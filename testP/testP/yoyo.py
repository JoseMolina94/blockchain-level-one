from django.http import HttpResponse

def treeJs(request):

    js="""
    
    <script type="module">

 

            import * as THREE from 'https://cdn.skypack.dev/three';

 

            let camera, scene, renderer;

            let mesh;

 

            init();

            animate();

 

            function init() {

 

                camera = new THREE.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 1, 1000 );

                camera.position.z = 400;

 

                scene = new THREE.Scene();

 

                const geometry = new THREE.BoxGeometry( 100, 100, 100 );

                const material = new THREE.MeshBasicMaterial( { color: "blue" } );

 

                mesh = new THREE.Mesh( geometry, material );

                scene.add( mesh );

 

                renderer = new THREE.WebGLRenderer( { antialias: true } );

                renderer.setPixelRatio( window.devicePixelRatio );

                renderer.setSize( window.innerWidth, window.innerHeight );

                document.body.appendChild( renderer.domElement );

 

                window.addEventListener( 'resize', onWindowResize );

 

            }

 

            function onWindowResize() {

 

                camera.aspect = window.innerWidth / window.innerHeight;

                camera.updateProjectionMatrix();

 

                renderer.setSize( window.innerWidth, window.innerHeight );

 

            }

 

            function animate() {

 

                requestAnimationFrame( animate );

 

                mesh.rotation.x += 0.05;

                mesh.rotation.y += 0.05;

 

                renderer.render( scene, camera );

 

            }

 

        </script>
        <canvas width='300' height='300' onload='init()' />

    """

    return HttpResponse(js)