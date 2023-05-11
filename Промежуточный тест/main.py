import db3
import matplotlib.pyplot as plt
import imag

user_id = 111

plt = imag.plt_result(user_id)
imag.save_plt_in_disc(plt,user_id)
db3.saved_img_in_db(user_id)

print(db3.giv_link_img_from_db(user_id))

