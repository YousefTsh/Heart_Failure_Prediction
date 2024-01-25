from fpdf import FPDF
import plotting as plot



def generate_report(predicition,age, ejection_fraction, serum_creatinine, platelets, serum_sodium, file_path):
	pdf = FPDF()
	pdf.add_page()
	pdf.set_xy(0, 0)

	pdf.set_font('arial', 'B',22)
	pdf.cell(45)
	pdf.cell(120, 15, "Heart Failure Predictor Report", 0, 1, 'C')

	pdf.set_font('arial', '', 12)
	pdf.cell(90, 16, "Your calculated chance of heart failure is:", 0, 1)

	pdf.set_font('arial', 'B', 20)
	pdf.cell(80)
	pdf.cell(30, 16, str(predicition) + "%", 0, 1, 'C')



	pdf.dashed_line(0, 52, 500, 52, 1, 1)

	pdf.set_font('arial', 'B', 12)
	pdf.cell(60, 46, "Attributes and correlation:", 0, 1)

	pdf.cell(1, 100, "", 0, 1)

	plot.plotHeatMap()

	pdf.image('plots/heatmap.png', x=20, y=75, w=200) #height is auto calculated

	pdf.set_font('arial', 'B', 8)

	pdf.cell(70, 0, '', 0, 0)
	pdf.set_text_color(102, 149, 209)
	pdf.cell(50, 46, "Fig. 1: this figure shows all the attributes including predicition and the correlation", 0, 1, 'C')


	pdf.add_page()
	pdf.set_xy(0,0)



	pdf.set_font('arial', 'B', 12)
	pdf.cell(10)
	pdf.set_text_color(0,0,0)
	pdf.cell(60, 46, "Model's Three biggest factors", 0, 1)

	plot.plotRegAge(age)
	pdf.image('plots/agereg.png', x=45, y=30, w=110)

	pdf.cell(70, 75, '', 0, 1)
	pdf.set_font('arial', 'B', 8)
	pdf.set_text_color(102, 149, 209)
	pdf.cell(67, 0, '', 0, 0)
	pdf.cell(50, 46, "Fig. 2: Event predicition using Age factor only", 0, 1, 'C')



	ejection_fraction_reg = plot.plotRegEjection(ejection_fraction)
	pdf.image('plots/ejectionreg.png', x=45, y=150, w=110)

	pdf.cell(70, 95, '', 0, 1)
	pdf.set_font('arial', 'B', 8)
	pdf.set_text_color(102, 149, 209)
	pdf.cell(67, 0, '', 0, 0)
	pdf.cell(50, 7, "Fig. 3: Event predicition using Ejection fraction factor only", 0, 1, 'C')

	pdf.set_text_color(102, 149, 209)
	pdf.cell(67, 0, '', 0, 0)
	#put the actual ejection fraction precentage in the following cell
	pdf.cell(50, 7, f"Note: this means having {ejection_fraction} % ejection fraction will lower your failure chance by {round(ejection_fraction_reg, 2)}", 0, 1, 'C')


	pdf.add_page()
	pdf.set_xy(0,0)

	plot.plotRegSerum(serum_creatinine)
	pdf.image('plots/serumreg.png', x=45, y=10, w=110)

	pdf.cell(70, 120, '', 0, 1)
	pdf.set_font('arial', 'B', 8)
	pdf.set_text_color(102, 149, 209)
	pdf.cell(67, 0, '', 0, 0)
	pdf.cell(50, 7, "Fig. 4: Event predicition using Serum Creatinine factor only", 0, 1, 'C')


	pdf.dashed_line(0, 135, 500, 135, 1, 1)


	pdf.set_text_color(0, 0, 0)
	pdf.set_font('arial', 'B', 12)
	pdf.cell(1, 15, '', 0, 1)
	pdf.cell(50, 7, "General Diagonsis", 0, 1)

	diagnosis_list = plot.diagnosis(ejection_fraction, platelets, serum_creatinine, serum_sodium)

	pdf.set_text_color(102, 149, 209)
	pdf.set_font('arial', 'B', 10)
	for i in diagnosis_list:
		pdf.cell(1, 10, '', 0, 1)
		pdf.cell(10, 0, '', 0, 0)
		pdf.cell(50, 7, chr(149) + " "+ i, 0, 1)


	pdf.output(rf'{file_path}', 'F')