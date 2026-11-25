import * as THREE from 'three';

/**
 * 3D Surface Visualizer for f(x,y) = x^2 + xy + y^2
 * Mathematical coordinate system:
 * In 3D graphics: Y is typically up. Here:
 * Three.js X = Math x
 * Three.js Y = Math z (Height output of function)
 * Three.js Z = Math y
 */
export class SurfaceVisualizer {
  constructor(containerElement) {
    this.container = containerElement;
    
    // State
    this.x = 1.0;
    this.y = 2.0;
    this.h = 0.5; // step for secant
    this.holdY = true;
    this.holdX = false;
    this.showTangentLine = true;
    this.showSecantLine = true;
    this.showTangentPlane = false;
    this.showCrossSectionPlane = true;
    this.activeMode = 'both'; // 'x', 'y', or 'both'
    
    this.width = this.container.clientWidth || 800;
    this.height = this.container.clientHeight || 550;
    
    this.initScene();
    this.initLights();
    this.initCoordinateGrid();
    this.buildSurface();
    this.buildDynamicVisuals();
    this.setupInteraction();
    
    this.animate = this.animate.bind(this);
    this.isAnimating = true;
    requestAnimationFrame(this.animate);
    
    window.addEventListener('resize', () => this.onResize());
  }

  // Pure mathematical functions
  static f(x, y) {
    return x * x + x * y + y * y;
  }

  static df_dx(x, y) {
    return 2 * x + y;
  }

  static df_dy(x, y) {
    return x + 2 * y;
  }

  initScene() {
    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(0x030712);
    this.scene.fog = new THREE.FogExp2(0x030712, 0.015);

    this.camera = new THREE.PerspectiveCamera(45, this.width / this.height, 0.1, 1000);
    // Position camera for an informative 3D isometric-style view
    this.camera.position.set(16, 14, 18);
    
    this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'high-performance' });
    this.renderer.setSize(this.width, this.height);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.renderer.shadowMap.enabled = true;
    this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    this.container.appendChild(this.renderer.domElement);

    // Root group for rotation and zoom
    this.worldGroup = new THREE.Group();
    this.scene.add(this.worldGroup);
  }

  initLights() {
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
    this.scene.add(ambientLight);

    const mainLight = new THREE.DirectionalLight(0xffffff, 1.2);
    mainLight.position.set(20, 30, 20);
    mainLight.castShadow = true;
    mainLight.shadow.mapSize.width = 2048;
    mainLight.shadow.mapSize.height = 2048;
    this.scene.add(mainLight);

    const cyanRim = new THREE.PointLight(0x38bdf8, 2, 50);
    cyanRim.position.set(-15, 10, -15);
    this.scene.add(cyanRim);

    const purpleRim = new THREE.PointLight(0xc084fc, 2, 50);
    purpleRim.position.set(15, 5, -15);
    this.scene.add(purpleRim);
  }

  initCoordinateGrid() {
    // Grid floor at z=0 (Three.js Y=0)
    const gridHelper = new THREE.GridHelper(16, 16, 0x334155, 0x1e293b);
    gridHelper.position.y = 0;
    this.worldGroup.add(gridHelper);

    // Coordinate Axes
    // X axis (Red/Cyan) -> Three.js X
    // Y axis (Green/Purple) -> Three.js Z
    // Z axis (Blue/Yellow vertical) -> Three.js Y
    const axisMaterialX = new THREE.LineBasicMaterial({ color: 0x38bdf8, linewidth: 2 });
    const axisMaterialY = new THREE.LineBasicMaterial({ color: 0xc084fc, linewidth: 2 });
    const axisMaterialZ = new THREE.LineBasicMaterial({ color: 0xf59e0b, linewidth: 2 });

    const createAxis = (start, end, mat) => {
      const geo = new THREE.BufferGeometry().setFromPoints([start, end]);
      return new THREE.Line(geo, mat);
    };

    this.worldGroup.add(createAxis(new THREE.Vector3(-4, 0, 0), new THREE.Vector3(5, 0, 0), axisMaterialX)); // Math x
    this.worldGroup.add(createAxis(new THREE.Vector3(0, 0, -4), new THREE.Vector3(0, 0, 5), axisMaterialY)); // Math y
    this.worldGroup.add(createAxis(new THREE.Vector3(0, 0, 0), new THREE.Vector3(0, 16, 0), axisMaterialZ));  // Math z (height)

    // Add 3D text/axis sprites
    this.createAxisLabels();
  }

  createAxisLabels() {
    const makeTextSprite = (text, colorStr) => {
      const canvas = document.createElement('canvas');
      canvas.width = 128;
      canvas.height = 64;
      const ctx = canvas.getContext('2d');
      ctx.font = 'bold 36px Inter, sans-serif';
      ctx.fillStyle = colorStr;
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(text, 64, 32);

      const texture = new THREE.CanvasTexture(canvas);
      const spriteMat = new THREE.SpriteMaterial({ map: texture, transparent: true });
      const sprite = new THREE.Sprite(spriteMat);
      sprite.scale.set(2, 1, 1);
      return sprite;
    };

    const labelX = makeTextSprite('+X', '#38bdf8');
    labelX.position.set(5.5, 0.3, 0);
    this.worldGroup.add(labelX);

    const labelY = makeTextSprite('+Y', '#c084fc');
    labelY.position.set(0, 0.3, 5.5);
    this.worldGroup.add(labelY);

    const labelZ = makeTextSprite('Z = f(x,y)', '#f59e0b');
    labelZ.position.set(0, 16.5, 0);
    this.worldGroup.add(labelZ);
  }

  buildSurface() {
    // Math domain: x in [-3, 3], y in [-3, 3]
    const xMin = -3, xMax = 3;
    const yMin = -3, yMax = 3;
    const segments = 60;
    
    const geometry = new THREE.PlaneGeometry(xMax - xMin, yMax - yMin, segments, segments);
    // Rotate plane so it lies horizontally (normal pointing UP in Three.js Y)
    geometry.rotateX(-Math.PI / 2);

    const pos = geometry.attributes.position;
    const colors = [];
    const color = new THREE.Color();

    for (let i = 0; i < pos.count; i++) {
      const uX = pos.getX(i);
      const uY = pos.getZ(i); // Note: Three.js Z corresponds to Math y
      const uZ = SurfaceVisualizer.f(uX, uY);
      pos.setY(i, uZ); // Set height

      // Color mapping based on height z: deep indigo to bright emerald
      const normHeight = Math.min(Math.max(uZ / 20, 0), 1);
      color.setHSL(0.6 - normHeight * 0.45, 0.85, 0.45 + normHeight * 0.15);
      colors.push(color.r, color.g, color.b);
    }
    geometry.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));
    geometry.computeVertexNormals();

    const material = new THREE.MeshStandardMaterial({
      vertexColors: true,
      side: THREE.DoubleSide,
      roughness: 0.35,
      metalness: 0.25,
      wireframe: false,
      transparent: true,
      opacity: 0.88,
    });

    this.surfaceMesh = new THREE.Mesh(geometry, material);
    this.worldGroup.add(this.surfaceMesh);

    // Surface wireframe overlay for depth perception
    const wireMat = new THREE.MeshBasicMaterial({
      color: 0x94a3b8,
      wireframe: true,
      transparent: true,
      opacity: 0.12
    });
    this.wireMesh = new THREE.Mesh(geometry, wireMat);
    this.worldGroup.add(this.wireMesh);
  }

  buildDynamicVisuals() {
    // 1. Highlighted point P(x, y, z)
    const pointGeo = new THREE.SphereGeometry(0.22, 32, 32);
    const pointMat = new THREE.MeshStandardMaterial({
      color: 0xef4444,
      emissive: 0xff0000,
      emissiveIntensity: 0.8,
      roughness: 0.2
    });
    this.pointMesh = new THREE.Mesh(pointGeo, pointMat);
    this.worldGroup.add(this.pointMesh);

    // Point halo ring
    const ringGeo = new THREE.RingGeometry(0.35, 0.45, 32);
    const ringMat = new THREE.MeshBasicMaterial({ color: 0xffffff, side: THREE.DoubleSide, transparent: true, opacity: 0.75 });
    this.ringMesh = new THREE.Mesh(ringGeo, ringMat);
    this.ringMesh.rotation.x = Math.PI / 2;
    this.worldGroup.add(this.ringMesh);

    // Vertical indicator line dropping from P down to xy-plane
    const dropLineGeo = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(), new THREE.Vector3()]);
    this.dropLine = new THREE.Line(dropLineGeo, new THREE.LineDashedMaterial({ color: 0xef4444, dashSize: 0.2, gapSize: 0.2, opacity: 0.6, transparent: true }));
    this.dropLine.computeLineDistances();
    this.worldGroup.add(this.dropLine);

    // 2. Cross-sectional curves
    // Curve for Y = constant (moving x): Cyan
    const curveGeoX = new THREE.BufferGeometry();
    const curveMatX = new THREE.LineBasicMaterial({ color: 0x38bdf8, linewidth: 4 });
    this.curveLineX = new THREE.Line(curveGeoX, curveMatX);
    this.worldGroup.add(this.curveLineX);

    // Curve for X = constant (moving y): Purple
    const curveGeoY = new THREE.BufferGeometry();
    const curveMatY = new THREE.LineBasicMaterial({ color: 0xc084fc, linewidth: 4 });
    this.curveLineY = new THREE.Line(curveGeoY, curveMatY);
    this.worldGroup.add(this.curveLineY);

    // 3. Tangent lines
    // Tangent in x-direction: slope = 2x+y
    const tanGeoX = new THREE.BufferGeometry();
    const tanMatX = new THREE.LineBasicMaterial({ color: 0x38bdf8, linewidth: 3 });
    this.tangentLineX = new THREE.Line(tanGeoX, tanMatX);
    this.worldGroup.add(this.tangentLineX);

    // Tangent in y-direction: slope = x+2y
    const tanGeoY = new THREE.BufferGeometry();
    const tanMatY = new THREE.LineBasicMaterial({ color: 0xc084fc, linewidth: 3 });
    this.tangentLineY = new THREE.Line(tanGeoY, tanMatY);
    this.worldGroup.add(this.tangentLineY);

    // 4. Secant lines (Limit demonstration)
    const secGeoX = new THREE.BufferGeometry();
    const secMatX = new THREE.LineDashedMaterial({ color: 0x06b6d4, dashSize: 0.3, gapSize: 0.15, linewidth: 2 });
    this.secantLineX = new THREE.Line(secGeoX, secMatX);
    this.worldGroup.add(this.secantLineX);

    const secGeoY = new THREE.BufferGeometry();
    const secMatY = new THREE.LineDashedMaterial({ color: 0xa855f7, dashSize: 0.3, gapSize: 0.15, linewidth: 2 });
    this.secantLineY = new THREE.Line(secGeoY, secMatY);
    this.worldGroup.add(this.secantLineY);

    // 5. Cross-sectional cutting planes
    const planeGeo = new THREE.PlaneGeometry(6.5, 18);
    const planeMatX = new THREE.MeshBasicMaterial({
      color: 0x0284c7,
      transparent: true,
      opacity: 0.22,
      side: THREE.DoubleSide,
      depthWrite: false
    });
    this.cuttingPlaneX = new THREE.Mesh(planeGeo, planeMatX);
    this.worldGroup.add(this.cuttingPlaneX);

    const planeMatY = new THREE.MeshBasicMaterial({
      color: 0x7c3aed,
      transparent: true,
      opacity: 0.22,
      side: THREE.DoubleSide,
      depthWrite: false
    });
    this.cuttingPlaneY = new THREE.Mesh(planeGeo, planeMatY);
    this.cuttingPlaneY.rotation.y = Math.PI / 2;
    this.worldGroup.add(this.cuttingPlaneY);

    // 6. Tangent plane at (x, y)
    const tanPlaneGeo = new THREE.PlaneGeometry(3.6, 3.6, 12, 12);
    const tanPlaneMat = new THREE.MeshStandardMaterial({
      color: 0xf59e0b,
      roughness: 0.4,
      metalness: 0.1,
      transparent: true,
      opacity: 0.45,
      side: THREE.DoubleSide
    });
    this.tangentPlaneMesh = new THREE.Mesh(tanPlaneGeo, tanPlaneMat);
    this.worldGroup.add(this.tangentPlaneMesh);

    // Initial update of geometry
    this.updateVisuals();
  }

  updateVisuals() {
    const x0 = this.x;
    const y0 = this.y;
    const z0 = SurfaceVisualizer.f(x0, y0);
    const slopeX = SurfaceVisualizer.df_dx(x0, y0);
    const slopeY = SurfaceVisualizer.df_dy(x0, y0);

    // 1. Update point position
    this.pointMesh.position.set(x0, z0, y0);
    this.ringMesh.position.set(x0, z0 + 0.02, y0);

    // Drop line from (x0, z0, y0) to (x0, 0, y0)
    const dropPts = [new THREE.Vector3(x0, z0, y0), new THREE.Vector3(x0, 0, y0)];
    this.dropLine.geometry.setFromPoints(dropPts);
    this.dropLine.computeLineDistances();

    // 2. Update Cross Section Curve for y = y0 (varying x)
    const ptsX = [];
    for (let u = -3; u <= 3; u += 0.08) {
      ptsX.push(new THREE.Vector3(u, SurfaceVisualizer.f(u, y0), y0));
    }
    this.curveLineX.geometry.dispose();
    this.curveLineX.geometry = new THREE.BufferGeometry().setFromPoints(ptsX);
    this.curveLineX.visible = (this.activeMode === 'x' || this.activeMode === 'both');

    // 3. Update Cross Section Curve for x = x0 (varying y)
    const ptsY = [];
    for (let v = -3; v <= 3; v += 0.08) {
      ptsY.push(new THREE.Vector3(x0, SurfaceVisualizer.f(x0, v), v));
    }
    this.curveLineY.geometry.dispose();
    this.curveLineY.geometry = new THREE.BufferGeometry().setFromPoints(ptsY);
    this.curveLineY.visible = (this.activeMode === 'y' || this.activeMode === 'both');

    // 4. Update Tangent Lines
    const L = 1.8; // length of tangent segment
    // Tangent along X: (x0 + t, z0 + slopeX * t, y0)
    const tanPtsX = [
      new THREE.Vector3(x0 - L, z0 - slopeX * L, y0),
      new THREE.Vector3(x0 + L, z0 + slopeX * L, y0)
    ];
    this.tangentLineX.geometry.dispose();
    this.tangentLineX.geometry = new THREE.BufferGeometry().setFromPoints(tanPtsX);
    this.tangentLineX.visible = this.showTangentLine && (this.activeMode === 'x' || this.activeMode === 'both');

    // Tangent along Y: (x0, z0 + slopeY * t, y0 + t)
    const tanPtsY = [
      new THREE.Vector3(x0, z0 - slopeY * L, y0 - L),
      new THREE.Vector3(x0, z0 + slopeY * L, y0 + L)
    ];
    this.tangentLineY.geometry.dispose();
    this.tangentLineY.geometry = new THREE.BufferGeometry().setFromPoints(tanPtsY);
    this.tangentLineY.visible = this.showTangentLine && (this.activeMode === 'y' || this.activeMode === 'both');

    // 5. Update Secant Lines (approaching tangent as h -> 0)
    const h = this.h;
    if (Math.abs(h) > 0.001) {
      // Secant X: from (x0, y0, z0) to (x0 + h, y0, f(x0+h, y0))
      const zH_X = SurfaceVisualizer.f(x0 + h, y0);
      const secSlopeX = (zH_X - z0) / h;
      const secPtsX = [
        new THREE.Vector3(x0 - 0.5, z0 - secSlopeX * 0.5, y0),
        new THREE.Vector3(x0 + h + 0.5, z0 + secSlopeX * (h + 0.5), y0)
      ];
      this.secantLineX.geometry.dispose();
      this.secantLineX.geometry = new THREE.BufferGeometry().setFromPoints(secPtsX);
      this.secantLineX.computeLineDistances();
      this.secantLineX.visible = this.showSecantLine && (this.activeMode === 'x' || this.activeMode === 'both');

      // Secant Y: from (x0, y0, z0) to (x0, y0 + h, f(x0, y0+h))
      const zH_Y = SurfaceVisualizer.f(x0, y0 + h);
      const secSlopeY = (zH_Y - z0) / h;
      const secPtsY = [
        new THREE.Vector3(x0, z0 - secSlopeY * 0.5, y0 - 0.5),
        new THREE.Vector3(x0, z0 + secSlopeY * (h + 0.5), y0 + h + 0.5)
      ];
      this.secantLineY.geometry.dispose();
      this.secantLineY.geometry = new THREE.BufferGeometry().setFromPoints(secPtsY);
      this.secantLineY.computeLineDistances();
      this.secantLineY.visible = this.showSecantLine && (this.activeMode === 'y' || this.activeMode === 'both');
    }

    // 6. Update Cutting Planes
    // Cutting plane X: constant Y = y0. Plane runs in X (horizontal) and Z (vertical)
    this.cuttingPlaneX.position.set(0, 9, y0);
    this.cuttingPlaneX.visible = this.showCrossSectionPlane && (this.activeMode === 'x' || this.activeMode === 'both');

    // Cutting plane Y: constant X = x0. Plane runs in Y (depth) and Z (vertical)
    this.cuttingPlaneY.position.set(x0, 9, 0);
    this.cuttingPlaneY.visible = this.showCrossSectionPlane && (this.activeMode === 'y' || this.activeMode === 'both');

    // 7. Update Tangent Plane
    // Tangent plane equation: z - z0 = fx*(x - x0) + fy*(y - y0)
    // Normal vector to surface is N = (-fx, 1, -fy) in math coords (X, Z-height, Y-depth)
    // In Three.js: (Nx, Ny, Nz) = (-slopeX, 1, -slopeY).normalize()
    this.tangentPlaneMesh.position.set(x0, z0, y0);
    const normal = new THREE.Vector3(-slopeX, 1, -slopeY).normalize();
    // Default plane geometry normal in Three.js is (0, 0, 1). Orient to our surface normal:
    this.tangentPlaneMesh.quaternion.setFromUnitVectors(new THREE.Vector3(0, 0, 1), normal);
    this.tangentPlaneMesh.visible = this.showTangentPlane;
  }

  setupInteraction() {
    let isDragging = false;
    let prevMouseX = 0;
    let prevMouseY = 0;

    const dom = this.renderer.domElement;

    dom.addEventListener('mousedown', (e) => {
      isDragging = true;
      prevMouseX = e.clientX;
      prevMouseY = e.clientY;
    });

    window.addEventListener('mousemove', (e) => {
      if (!isDragging) return;
      const deltaX = e.clientX - prevMouseX;
      const deltaY = e.clientY - prevMouseY;
      prevMouseX = e.clientX;
      prevMouseY = e.clientY;

      this.worldGroup.rotation.y += deltaX * 0.008;
      this.worldGroup.rotation.x += deltaY * 0.008;

      // Clamp vertical rotation
      this.worldGroup.rotation.x = Math.max(-Math.PI / 4, Math.min(Math.PI / 3, this.worldGroup.rotation.x));
    });

    window.addEventListener('mouseup', () => {
      isDragging = false;
    });

    // Touch support for mobile / tablet
    dom.addEventListener('touchstart', (e) => {
      if (e.touches.length === 1) {
        isDragging = true;
        prevMouseX = e.touches[0].clientX;
        prevMouseY = e.touches[0].clientY;
      }
    }, { passive: true });

    window.addEventListener('touchmove', (e) => {
      if (!isDragging || e.touches.length !== 1) return;
      const deltaX = e.touches[0].clientX - prevMouseX;
      const deltaY = e.touches[0].clientY - prevMouseY;
      prevMouseX = e.touches[0].clientX;
      prevMouseY = e.touches[0].clientY;

      this.worldGroup.rotation.y += deltaX * 0.01;
      this.worldGroup.rotation.x += deltaY * 0.01;
      this.worldGroup.rotation.x = Math.max(-Math.PI / 4, Math.min(Math.PI / 3, this.worldGroup.rotation.x));
    }, { passive: true });

    window.addEventListener('touchend', () => {
      isDragging = false;
    });

    // Mouse wheel zoom
    dom.addEventListener('wheel', (e) => {
      e.preventDefault();
      const zoomFactor = e.deltaY * 0.015;
      const newFov = this.camera.fov + zoomFactor;
      this.camera.fov = Math.max(20, Math.min(75, newFov));
      this.camera.updateProjectionMatrix();
    }, { passive: false });
  }

  // Public control methods
  setX(val) {
    this.x = parseFloat(val);
    this.updateVisuals();
  }

  setY(val) {
    this.y = parseFloat(val);
    this.updateVisuals();
  }

  setH(val) {
    this.h = parseFloat(val);
    this.updateVisuals();
  }

  setMode(mode) {
    this.activeMode = mode;
    this.updateVisuals();
  }

  toggleTangentLine(show) {
    this.showTangentLine = show;
    this.updateVisuals();
  }

  toggleSecantLine(show) {
    this.showSecantLine = show;
    this.updateVisuals();
  }

  toggleTangentPlane(show) {
    this.showTangentPlane = show;
    this.updateVisuals();
  }

  toggleCuttingPlane(show) {
    this.showCrossSectionPlane = show;
    this.updateVisuals();
  }

  reset() {
    this.x = 1.0;
    this.y = 2.0;
    this.h = 0.5;
    this.activeMode = 'both';
    this.showTangentLine = true;
    this.showSecantLine = true;
    this.showTangentPlane = false;
    this.showCrossSectionPlane = true;
    this.worldGroup.rotation.set(0.2, -0.4, 0);
    this.camera.position.set(16, 14, 18);
    this.camera.fov = 45;
    this.camera.updateProjectionMatrix();
    this.updateVisuals();
  }

  onResize() {
    this.width = this.container.clientWidth;
    this.height = this.container.clientHeight;
    this.camera.aspect = this.width / this.height;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(this.width, this.height);
  }

  animate() {
    if (!this.isAnimating) return;
    requestAnimationFrame(this.animate);

    // Subtle breathing animation on halo ring
    if (this.ringMesh) {
      const s = 1 + Math.sin(Date.now() * 0.005) * 0.08;
      this.ringMesh.scale.set(s, s, s);
    }

    this.renderer.render(this.scene, this.camera);
  }

  destroy() {
    this.isAnimating = false;
    this.renderer.dispose();
  }
}
