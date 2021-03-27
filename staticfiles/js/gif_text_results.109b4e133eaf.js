let url = window.location.href
let text = url.split("/")

let text_info = document.getElementById('text_info')
let icon_text_info = document.getElementById('icon_text_info')
let gif_expl = document.getElementById('gif_info')

if(text_info) {
  if(text[text.length - 1] === VIEW || text[text.length - 1] === VIEW + "#") {
    icon_text_info.style.display = "none"
    if(window.innerWidth > 768) {
      //gif_expl.src = "https://media.giphy.com/media/oisvriIdlTYZoGxWeT/giphy.gif"
      gif_expl.src = "static/images/gifs/gif2.gif"
      gif_expl.style.maxWidth = "676px"
      gif_expl.style.margin = "auto"
    }else {
      //gif_expl.src = "https://media.giphy.com/media/kC7ScGLhvKG2n95Vjk/giphy.gif"
      gif_expl.src = "static/images/gifs/gif1.gif"
      gif_expl.style.minWidth = "280px"
      gif_expl.style.margin = "auto"
    }
  } else {
    text_info.textContent="No se encontraron resultados para esta búsqueda."
    icon_text_info.style.display = "block"
    gif_expl.style.display = "none"
  }
}