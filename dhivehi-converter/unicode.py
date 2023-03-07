import re

class DhivehiConverter:
    def accent_to_unicode(text, reverse=True):
        if text is not None:
            text = text.replace('h', 'ހ')
            text = text.replace('S', 'ށ')
            text = text.replace('n', 'ނ')
            text = text.replace('r', 'ރ')
            text = text.replace('b', 'ބ')
            text = text.replace('L', 'ޅ')
            text = text.replace('k', 'ކ')
            text = text.replace('a', 'އ')
            text = text.replace('v', 'ވ')
            text = text.replace('m', 'މ')
            text = text.replace('M', 'މ')
            text = text.replace('f', 'ފ')
            text = text.replace('d', 'ދ')
            text = text.replace('t', 'ތ')
            text = text.replace('l', 'ލ')
            text = text.replace('g', 'ގ')
            text = text.replace('N', 'ޏ')
            text = text.replace('s', 'ސ')
            text = text.replace('D', 'ޑ')
            text = text.replace('z', 'ޒ')
            text = text.replace('T', 'ޓ')
            text = text.replace('y', 'ޔ')
            text = text.replace('p', 'ޕ')
            text = text.replace('P', 'ޕ')
            text = text.replace('j', 'ޖ')
            text = text.replace('C', 'ޗ')
            text = text.replace('H', 'ޙ')
            text = text.replace('K', 'ޚ')
            text = text.replace('R', 'ޜ')
            text = text.replace('A', 'ޢ')
            text = text.replace('G', 'ޣ')
            text = text.replace('V', 'ޥ')
            text = text.replace('J', 'ޛ')
            text = text.replace('X', 'ޘ')
            text = text.replace('Y', 'ޠ')
            text = text.replace('Z', 'ޡ')
            text = text.replace('q', 'ޤ')
            text = text.replace('x', 'ޝ')
            text = text.replace('B', 'ޞ')
            text = text.replace('F', 'ޟ')
            text = text.replace('w', 'ަ')
            text = text.replace('W', 'ާ')
            text = text.replace('i', 'ި')
            text = text.replace('I', 'ީ')
            text = text.replace('u', 'ު')
            text = text.replace('U', 'ޫ')
            text = text.replace('e', 'ެ')
            text = text.replace('E', 'ޭ')
            text = text.replace('o', 'ޮ')
            text = text.replace('O', 'ޯ')
            text = text.replace('c', 'ް')
            text = text.replace('Q', 'ﷲ')

            if reverse is True:
                return ''.join(s if s.isdigit() else s[::-1] for s in reversed(re.split('(\d+)', text)))
            else:
                return text[::-1]


    def ascii_to_unicode(text, reverse=True):
        if text is not None:
            text = text.replace('h', 'ހ')
            text = text.replace('S', 'ށ')
            text = text.replace('n', 'ނ')
            text = text.replace('r', 'ރ')
            text = text.replace('b', 'ބ')
            text = text.replace('L', 'ޅ')
            text = text.replace('k', 'ކ')
            text = text.replace('a', 'ަ')
            text = text.replace('v', 'ވ')
            text = text.replace('m', 'މ')
            text = text.replace('M', 'ޟ')
            text = text.replace('f', 'ފ')
            text = text.replace('d', 'ދ')
            text = text.replace('t', 'ތ')
            text = text.replace('l', 'ލ')
            text = text.replace('g', 'ގ')
            text = text.replace('N', 'ޏ')
            text = text.replace('s', 'ސ')
            text = text.replace('D', 'ޑ')
            text = text.replace('z', 'ޒ')
            text = text.replace('T', 'ޓ')
            text = text.replace('y', 'ޔ')
            text = text.replace('p', 'ޕ')
            text = text.replace('j', 'ޖ')
            text = text.replace('C', 'ޝ')
            text = text.replace('X', 'ޘ')
            text = text.replace('H', 'ޙ')
            text = text.replace('K', 'ޚ')
            text = text.replace('J', 'ޛ')
            text = text.replace('R', 'ޜ')
            text = text.replace('x', '×')
            text = text.replace('B', 'ޞ')
            text = text.replace('F', 'ﷲ')
            text = text.replace('Y', 'ޠ')
            text = text.replace('Z', 'ޡ')
            text = text.replace('A', 'ާ')
            text = text.replace('G', 'ޣ')
            text = text.replace('q', 'ް')
            text = text.replace('Q', 'ޤ')
            text = text.replace('V', 'ޥ')
            text = text.replace('w', 'އ')
            text = text.replace('W', 'ޢ')
            text = text.replace('i', 'ި')
            text = text.replace('I', 'ީ')
            text = text.replace('u', 'ު')
            text = text.replace('U', 'ޫ')
            text = text.replace('e', 'ެ')
            text = text.replace('E', 'ޭ')
            text = text.replace('o', 'ޮ')
            text = text.replace('O', 'ޯ')
            text = text.replace('c', 'ޗ')

            if reverse is True:
                return ''.join(s if s.isdigit() else s[::-1] for s in reversed(re.split('(\d+)', text[::-1])))
            else:
                return text[::-1][::-1]