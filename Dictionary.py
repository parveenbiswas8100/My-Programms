while(True):
    dic_list = {"Abandon":"to forsake(tyaag deena)", "Abash":"to put to shame(laajit karna)", "Abbreviate":"to shorten(km karna)","Abdal":"dervish(darvaish)","Abduct":"to kidnap(bagaa kar lay jana)", "Ability":"strength(takaat,shakti,yeigta)", "Additional":"add on, extra(athirikt)", "Burnt":"treated with fire(jalaa huaa)"}

    user_put = input("Enter your word:\n").capitalize()
    print(user_put, "means", dic_list[user_put])

    not1 = input("Do you want to search again(y/n):\n")
    if not1=='y':
        continue
    else:
        break