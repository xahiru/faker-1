from typing import Tuple

from .. import Provider as PersonProvider
# source: https://www.gov.mv/en/publications/baby-names

class Provider(PersonProvider):
    formats_female: Tuple[str, ...] = (
        "{{first_name_female}} {{last_name_female}}",
        "{{first_name_female}} {{first_names_male}}",
        "{{last_name_female}} {{first_names_male}}",
        "{{prefix_female}} {{first_name_female}} {{last_name_female}}",
    )

    formats_male: Tuple[str, ...] = (
        "{{first_name_male}} {{last_name}}",
        "{{prefix_male}} {{first_name_male}} {{last_name}}",
    )

    formats = formats_male + formats_female

    first_names_female: Tuple[str, ...] = (
        "ފާތުމަތު",
        "ހައްވަ",
        "އައިޝާ",
    )

    last_names_female: Tuple[str, ...] = (
        "ނިޒާމާ",
        "ރިޔާޝާ",
        "ޒުބޭދާ",
    )

    first_names_male: Tuple[str, ...] = (
        "އަހުމަދު",
        "އިބްރާހިމް",
        "ހުސައިން",
        "މުހައްމަދު",
        "އަލީ",
        "ހަސަން",
    )

    first_names = first_names_male + first_names_female

    last_names_male: Tuple[str, ...] = (
        "ނިޔާޒް",
        "ޝިފާޒް",
        "ޒިޔާދު",
        "ރުޝްދީ",
    )


    prefixes_female: Tuple[str, ...] = (
        "އަލްފާލިލާ",
        "ޑޮކްޓަރ",
        "އަލްއުސްތާޒާ",
    )
    prefixes_male: Tuple[str, ...] = ("ޑޮކްޓަރ", "އަލްއުސްތާޒް", "އަލްހާޖީ", "އަލްފާލިލް")
