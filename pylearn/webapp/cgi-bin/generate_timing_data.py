import cgi
import athletemodel
import yate

athletes=athletemodel.get_from_store()

form_data=cgi.FieldStorage()
athlete_name=form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header('timing data'))
print(yate.header("Athlete:"+athlete_name+",DOB:"+athletes[athlete_name].dob))
print(yate.para("the top times are:"))
print(yate.u_list(athletes[athlete_name].top3))
print(yate.include_footer({"home":"index.html","anthor":"generate_list.py"}))
