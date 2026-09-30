Insta_profile = {
   "user_name":"Kinza_coder",
   "followers":"50",
   "is_private":True
}
Insta_profile["followers"] = 100
Insta_profile["bio"] = "Learning_python"
del Insta_profile["followers"]
if "email" in Insta_profile:
    print("email is linked")
else:
    print("Security warning:email is missing")
for key , value in Insta_profile.items():
    print(f"{key}:{value}")
print(Insta_profile.values())


