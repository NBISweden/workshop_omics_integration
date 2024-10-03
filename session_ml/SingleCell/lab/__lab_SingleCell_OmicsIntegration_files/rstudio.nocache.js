

<!DOCTYPE html>
<html lang="en">

<head>
    <title>Login | SciLifeLab Serve (beta)</title>
    
    

    

<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<meta name="description" content="">
<meta name="author" content="">

<link rel="icon" href="/static/images/scilifelab_favicon.png" type="image/x-icon">

<script src="/static/js/js-utility.js"></script>
<script src="/static/js/bs-tooltip.js" defer></script>

<link href="/static/vendor/bootstrap-5.2.3-dist/css/bootstrap.min.css" rel="stylesheet">
<script src="/static/vendor/bootstrap-5.2.3-dist/js/bootstrap.bundle.min.js"></script>

<script src="/static/admin/js/vendor/jquery/jquery.min.js"></script>
<link href="/static/vendor/icons-1.10.3/font/bootstrap-icons.css" rel="stylesheet">

<link rel="stylesheet" href="/static/css/serve-colors.css">
<link rel="stylesheet" href="/static/css/serve-text.css">
<link rel="stylesheet" href="/static/css/serve-utilities.css">
<link rel="stylesheet" href="/static/css/serve-elements.css">
<link rel="stylesheet" href="/static/css/patterns.css">

<link href="/static/vendor/aos-2.3.4-dist/css/aos.css" rel="stylesheet">
<link rel="stylesheet" href="/static/css/dataTables.bootstrap5.min.css">
<script src="/static/js/jquery.dataTables.min.js"></script>
<script src="/static/js/dataTables.bootstrap5.min.js"></script>
<script src="/static/js/htmx.min.js"></script>

     
</head>

<body class="d-flex flex-column min-vh-100">

    

<nav class="bg-light shadow-sm mb-3 py-2">
    <div class="container">
        <div class="row">
            <div class="col-12 col-lg-3 d-flex align-items-center justify-content-lg-start justify-content-center py-2">
                <a href="/" class="navbar-brand w-100">
                    <img src="/static/images/scilifelab_serve_logo.svg" title="SciLifeLab Serve (beta)" style="width:100%; max-height:2.2rem">
                </a>
            </div>
        
            <div class="col-12 col-lg-9 d-flex justify-content-lg-end justify-content-center py-2">
                <ul class="nav text-center justify-content-center align-items-center">
                    <li class="nav-item">
                        <a class="nav-link" href="/home/" target="_self" title="Homepage">
                            <i class="fa-solid fa-home d-block mx-auto"></i>
                            Home
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/apps/" target="_self" title="Apps">
                            Apps
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/models/" target="_self" title="Models">
                            Models
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="/docs/" target="_self" title="User guide">
                            User guide
                        </a>
                    </li>
                    

                    <li class="nav-item ">
                        <a class="nav-link" href="/projects/" target="_self" title="My projects">
                            My projects
                        </a>
                    </li>
                    <li class="btn-group">
                        <button type="button" class="btn btn-profile dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false" title="rasools@chalmers.se">
                            <i class="bi bi-person-circle"></i> Profile
                        </button>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="/user/profile/"><i class="bi bi-person me-1"></i>My profile</a></li>
                            <li><a class="dropdown-item" href="/accounts/password_change/"><i class="bi bi-key me-1"></i>Change password</a></li>
                            <form action="/accounts/logout/" method="post">
                                <input type="hidden" name="csrfmiddlewaretoken" value="LX425096h0xyCcwGAcU4jPZxPP1aTbxqFXAr8R4c97HT4r9OR3hpTQ5xDyYqyNIA">
                                <li><button class="dropdown-item" type="submit"><i class="bi bi-box-arrow-right me-1"></i>Sign out</button></li>
                            </form>
                        </ul>
                    </li>


                    
                </ul>
            </div>
        
        </div>
    </div>
</nav>


  



    <main class="container mb-3">
    

<div class="container">
  <!-- Outer Row -->

  <div class="row justify-content-center">
    <div class="col-12 col-md-9">
      

      <div class="card border-0 shadow-lg my-5 py-5">
        <div class="card-body">
          <!-- Nested Row within Card Body -->
          <div class="col-lg-6 offset-lg-3">

            <div class="col text-center">
              <h2 class="text-dark mb-4">Log in</h2>
            </div>

            

            



            <div class="py-4 d-flex justify-content-center">

              <div class="w-100">
                <form method="post" action="/accounts/login/">
                  <input type="hidden" name="csrfmiddlewaretoken" value="LX425096h0xyCcwGAcU4jPZxPP1aTbxqFXAr8R4c97HT4r9OR3hpTQ5xDyYqyNIA">
                  <div class="form-group pb-2">
                    <label for="username-id">Email:</label>
                    <input type="email"
                           style="text-transform: lowercase" onchange="this.value = this.value.toLowerCase();"
                           class="form-control" id="username-id" name="username">
                  </div>
                  <div class="form-group pb-3">
                    <label for="password-id">Password:</label>
                    <input type="password" class="form-control" id="password-id" name="password">
                  </div>
                  <div class="form-group d-flex justify-content-center"><button type="submit"
                      class="btn btn-primary w-xs-100 px-5">Login</button></div>
                </form>
              </div>

            </div>
            <div class="text-center">
              <a href="/accounts/password_reset/">Forgot password?</a>
            </div>
            <div class="text-center">
              <a href="/signup/">Don't have an account? Sign up here</a>
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>

</div>




    </main>

    <div class="modal fade" id="modalConfirmDelete" tabindex="-1" aria-labelledby="modalConfirmDeleteLabel"
        aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="modalConfirmDeleteLabel"></h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">

                    <div class="row py-3">
                        <div id="modalConfirmDeleteBodyIcon"
                            class="col d-flex justify-content-center align-items-center"></div>
                    </div>

                    <div class="row">
                        <div class="col">
                            <p id="modalConfirmDeleteBodyText" class="text-center"></p>
                        </div>
                    </div>

                </div>
                <div id="modalConfirmDeleteFooter" class="modal-footer d-flex justify-content-between">
                </div>
            </div>
        </div>
    </div>

    






<div class="footer border-top bg-light text-muted small pt-4 mt-auto">

    <div class="container">

    
    

    <div class="row pb-2">
            <div class="col-md-2 col-lg-2 col-xl-1">
                <ul class="list-unstyled">
                    <li><a href="/home/">Home</a></li>
                    <li><a href="/about/">About</a></li>
                    <li><a href="/privacy/">Privacy policy</a></li>
                    <li><a href="/apps/">Public apps</a></li>
                    <li><a href="/models/">Public models</a></li>
                    <li><a href="/collections/">Collections</a></li>
                </ul>
            </div>
            <div class="col-md-2 col-lg-2 col-xl-1">
                <ul class="list-unstyled">
                    <li><a href="/docs/">User guide</a></li>
                    <li><a href="/teaching/">Teaching</a></li>
                    <li><a href="/news/">News</a></li>
                    <li><a href="/events/">Events</a></li>
                </ul>
            </div>
            <div class="col-lg-5 col-xl-7">
                <p>SciLifeLab Serve (beta) is developed and operated by the <a href="https://scilifelab.se/data" target="_blank">SciLifeLab Data Centre</a>. SciLifeLab Serve is free to use for all life science researchers affiliated with a Swedish research institution and their collaborators. The service is hosted on a Kubernetes cluster. The code behind SciLifeLab Serve is <a href="https://github.com/ScilifelabDataCentre/serve/">available on Github</a>.</p>
                <p>Please email <a href="mailto:serve@scilifelab.se">serve@scilifelab.se</a> with any questions.</p>
                <p>
                    version 2024-09-19 (v2.1.0-beta)
                    
                </p>
            </div>
            <div class="col-9 col-md-6 col-lg-3">
                <div class="row">
                    <div class="col">
                        <p>Supported by:</p>
                    </div>
                </div>
                <div class="row align-items-center">
                    <div class="col"><img class="img-fluid" src="/static/images/scilifelab_logo.png" alt="SciLifeLab"></div>
                    <div class="col"><img class="img-fluid" src="/static/images/ssf_logo.png" alt="Swedish Foundation for Strategic Research"></div>
                    <div class="col"><img class="img-fluid" src="/static/images/kaw_logo.png" alt="Knut and Alice Wallenberg Foundation"></div>
                </div>
            </div>
        </div>
    </div>
</div>


    
    <script>
        {
            const elements = document.querySelectorAll(".confirm-delete")

            const modal = new bootstrap.Modal(document.getElementById("modalConfirmDelete"), {});
            const modalTitle = document.getElementById("modalConfirmDeleteLabel")
            const modalBodyIcon = document.getElementById("modalConfirmDeleteBodyIcon")
            const modalBodyText = document.getElementById("modalConfirmDeleteBodyText")
            const modalFooter = document.getElementById("modalConfirmDeleteFooter")

            elements.forEach(element => {

                element.addEventListener("click", (e) => {

                    e.preventDefault();

                    removeAllChildNodes(modalBodyIcon)
                    removeAllChildNodes(modalFooter)

                    const { target } = e

                    const title = target.getAttribute("data-title") ?? "Do you really want to delete this?"
                    const text = target.getAttribute("data-text") ?? "Note that this is an irreversible action, it is not possible to recover a deleted item!"
                    const icon = target.getAttribute("data-icon") ?? "bi-exclamation-triangle"

                    const href = target.getAttribute("href")

                    modalTitle.innerText = title

                    const iElement = document.createElement("i")
                    iElement.className = `bi ${icon} fs-1`

                    modalBodyIcon.appendChild(iElement)

                    modalBodyText.innerText = text

                    const confirmBtnElement = document.createElement("button")
                    confirmBtnElement.classList = "btn btn-danger"
                    confirmBtnElement.setAttribute("type", "button")
                    confirmBtnElement.innerText = "Delete"

                    modalFooter.appendChild(confirmBtnElement)

                    const closeBtnElement = document.createElement("button")
                    closeBtnElement.className = "btn btn-primary"
                    closeBtnElement.setAttribute("type", "button")
                    closeBtnElement.setAttribute("data-bs-dismiss", "modal")
                    closeBtnElement.innerText = "Close"

                    modalFooter.appendChild(closeBtnElement)

                    confirmBtnElement.addEventListener("click", () => {
                        location.href = href
                    })

                    modal.show()
                })
            })
        }

        window.addEventListener('load', function () {
            let btnToTop = document.getElementById("btn-to-top");
            window.onscroll = function () {
                if (
                    (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) &&
                    window.innerWidth >= 768
                ) {
                    btnToTop.style.display = "block";
                } else {
                    btnToTop.style.display = "none";
                }
            };
            btnToTop.addEventListener("click", function () {
                document.body.scrollTop = 0;
                document.documentElement.scrollTop = 0;
            });
        })


        function copyClip(data, event) {
            var inputc = document.body.appendChild(document.createElement("input"));
            inputc.value = data;
            var scrollY = window.scrollY; // Store the current scroll position
            inputc.select();
            document.execCommand('copy');
            inputc.parentNode.removeChild(inputc);
            window.scrollTo(0, scrollY); // Restore the scroll position

                // Add confirmation tooltip
            var tooltip = document.createElement("div");
            tooltip.innerHTML = "Copied";
            tooltip.style.position = "fixed";
            tooltip.classList.add("badge", "bg-secondary", "text-white")

            tooltip.style.zIndex = "9999";
            document.body.appendChild(tooltip);

            // Position tooltip at the mouse click location
            tooltip.style.left = event.clientX + "px";
            tooltip.style.top = event.clientY + "px";
            tooltip.style.transform = "translate(-50%, -150%)"

            // Remove the tooltip after 2 seconds
            setTimeout(function() {
                tooltip.parentNode.removeChild(tooltip);
            }, 1000);
        }


    </script>

     

        <!-- Visitor analytics -->
    <script>
        var _paq = window._paq = window._paq || [];
        /* tracker methods like "setCustomDimension" should be called before "trackPageView" */
        _paq.push(["disableCookies"]);
        _paq.push(['trackPageView']);
        _paq.push(['enableLinkTracking']);
        (function () {
            var u = "//matomo.dckube.scilifelab.se/";
            _paq.push(['setTrackerUrl', u + 'matomo.php']);
            _paq.push(['setSiteId', '5']);
            var d = document, g = d.createElement('script'), s = d.getElementsByTagName('script')[0];
            g.async = true; g.src = u + 'matomo.js'; s.parentNode.insertBefore(g, s);
        })();
    </script>


    
    


    <button type="button" class="btn btn-secondary btn-lg btn-top" id="btn-to-top">
        <i class="bi bi-arrow-up"></i>
    </button>

    <script src="/static/vendor/aos-2.3.4-dist/js/aos.js"></script>
    <script>AOS.init({once: true});</script>

</body>

</html>
