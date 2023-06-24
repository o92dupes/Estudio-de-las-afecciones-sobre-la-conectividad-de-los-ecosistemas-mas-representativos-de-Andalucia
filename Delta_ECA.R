library(ggsankey)
library(ggplot2)
library(dplyr)
library(scales)
library(dummies)
library(kableExtra)
library(highcharter)

# Función para reescalar una variable entre un rango específico
rescale_variable <- function(x, new_min, new_max) {
  old_min <- min(x, na.rm = TRUE)
  old_max <- max(x, na.rm = TRUE)
  new_x <- (x - old_min) / (old_max - old_min) * (new_max - new_min) + new_min
  return(new_x)
}

setwd("G:/TFM/Resultados Restoration planner/P.halepensis/csv")

df1 <- read.csv("b_current_restoration_var.csv",sep = ",", dec = ".")
df1$ESCENARIO <- "00_CURRENT"
df1.selected <- select(df1, ESCENARIO, DELTA_ECA,RESTORE)

df2 <- read.csv("b_21-40ssp245_restoration_var.csv",sep = ",", dec = ".")
df2$ESCENARIO <- "21-40ssp245"
df2.selected <- select(df2, ESCENARIO, DELTA_ECA,RESTORE)

df3 <- read.csv("b_21-40ssp370_restoration_var.csv",sep = ",", dec = ".")
df3$ESCENARIO <- "21-40ssp370"
df3.selected <- select(df3, ESCENARIO, DELTA_ECA,RESTORE)

df4 <- read.csv("b_21-40ssp585_restoration_var.csv",sep = ",", dec = ".")
df4$ESCENARIO <- "21-40ssp585"
df4.selected <- select(df4, ESCENARIO, DELTA_ECA,RESTORE)

df5 <- read.csv("b_41-60ssp245_restoration_var.csv",sep = ",", dec = ".")
df5$ESCENARIO <- "41-60ssp245"
df5.selected <- select(df5, ESCENARIO, DELTA_ECA,RESTORE)

df6 <- read.csv("b_41-60ssp370_restoration_var.csv",sep = ",", dec = ".")
df6$ESCENARIO <- "41-60ssp370"
df6.selected <- select(df6, ESCENARIO, DELTA_ECA,RESTORE)

df7 <- read.csv("b_41-60ssp585_restoration_var.csv",sep = ",", dec = ".")
df7$ESCENARIO <- "41-60ssp585"
df7.selected <- select(df7, ESCENARIO, DELTA_ECA,RESTORE)

df8 <- read.csv("b_61-80ssp245_restoration_var.csv",sep = ",", dec = ".")
df8$ESCENARIO <- "61-80ssp245"
df8.selected <- select(df8, ESCENARIO, DELTA_ECA,RESTORE)

df9 <- read.csv("b_61-80ssp370_restoration_var.csv",sep = ",", dec = ".")
df9$ESCENARIO <- "61-80ssp370"
df9.selected <- select(df9, ESCENARIO, DELTA_ECA,RESTORE)

df10 <- read.csv("b_81-100ssp245_restoration_var.csv",sep = ",", dec = ".")
df10$ESCENARIO <- "81-100ssp245"
df10.selected <- select(df10, ESCENARIO, DELTA_ECA,RESTORE)

df.comb <- merge(df1.selected,df2.selected,all = TRUE)
df.comb2 <- merge(df.comb,df3.selected,all = TRUE)
df.comb3 <-merge(df.comb2,df4.selected,all = TRUE)
df.comb4 <-merge(df.comb3,df5.selected,all = TRUE)
df.comb5 <-merge(df.comb4,df6.selected,all = TRUE)
df.comb6 <-merge(df.comb5,df7.selected,all = TRUE)
df.comb7 <-merge(df.comb6,df8.selected,all = TRUE)
df.comb8 <-merge(df.comb7,df9.selected,all = TRUE)
df.def <-merge(df.comb8,df10.selected,all = TRUE)

# OTRA POSIBILIDAD PARA Combinar los dataframes
##  df.comb <- bind_rows(df1.selected, df2.selected, df3.selected)

# Crear el dataframe
df <- data.frame(
  ESCENARIO = df.def$ESCENARIO,
  DELTA_ECA = cut(rescale_variable(df.def$DELTA_ECA, 0, 100), breaks = seq(0, 100, by = 5), include.lowest = TRUE),
  RESTORE = df.def$RESTORE
)

# Convertir las variables a factores
df$ESCENARIO <- as.factor(df$ESCENARIO)
df$DELTA_ECA <- as.factor(df$DELTA_ECA)
df$RESTORE <- as.factor(df$RESTORE)

# Visualizar el dataframe
print(df)

sankey_df <- data_to_sankey(df)

hchart(
  sankey_df,
  type = "sankey",
  name = "Pesos de Delta_ECA - Restoration planner"
)  |>
  hc_title(text = "<b>Diagrama de Sankey</b>") |>
  hc_subtitle(text = "<i>DELTA_ECA - dataset Pinus halepensis</i>") |>
  hc_credits(enabled = TRUE, text = "TFM-Sergio Roque Duarte Pérez")
