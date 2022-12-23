class Address:
    def __init__(self, street, village, district, city, postcode, street2=None):
        self.street = street
        self.street2 = street2
        self.village = village
        self.district = district
        self.city = city
        self.postcode = postcode

    # kalau pakai string nanti kelihatan kurang rapi, dan penggunaan list dibawah ini supaya code terlihat lebih bagus
    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.village}, {self.district}, {self.city} {self.postcode}')
        return '\n'.join(lines)

class AddressBook:
    def __init__(self):
        self._employee_addresses = {
            1: Address('121 Admin Rd.', 'village', 'Concord', 'NH', '03301'),
            2: Address('67 Paperwork Ave', 'village', 'Manchester', 'NH', '03101'),
            3: Address('15 Rose St', 'village', 'Concord', 'NH', '03301', 'Apt. B-1'),
            4: Address('39 Sole St.', 'village', 'Concord', 'NH', '03301'),
            5: Address('99 Mountain Rd.', 'village', 'Concord', 'NH', '03301'),
        }

    def get_employee_address(self, employee_id):
        address = self._employee_addresses.get(employee_id)
        if not address:
            raise ValueError(employee_id)
        return address