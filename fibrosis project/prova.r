library(readxl)
setwd("C:/Users/MM/Downloads/")
arxiu_excel <- "FibroPredCODIFICADA.xlsx"
dd <- read_excel(arxiu_excel)

if ("Pathology pattern" %in% colnames(dd)) {
  valores_unicos <- unique(dd$'Pathology pattern')
  print(valores_unicos) 
} else {
  print("La columna 'pathology_pattern' no está en el archivo.")
}
  