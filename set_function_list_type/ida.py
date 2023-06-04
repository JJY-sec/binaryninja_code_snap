import idaapi
import idc

# 함수 테이블의 시작 주소입니다.
table_start = 0x00000001C004F600  # 실제 주소로 변경해주세요.

# 각 함수의 현재 프로토타입을 가져옵니다.
# 이 예제에서는 함수가 void function(int, int)라고 가정합니다.

new_func_type = idaapi.tinfo_t()

# 테이블의 각 함수에 대해 프로토타입을 변경합니다.
for i in range(0, 0x4A*8, 8):  # 64비트인 경우, range(0, 0x40, 8)
    # 함수 주소를 가져옵니다.
    func_ea = idc.get_qword(table_start + i)  # 64비트인 경우, idc.get_qword를 사용하세요.
    name = idc.get_name(func_ea, ida_name.GN_VISIBLE)
    # 현재 함수의 프로토타입을 가져옵니다.
    function_proto = f'NTSTATUS __fastcall {name}(PIRP Irp, _IO_STACK_LOCATION*);'
    print(function_proto)
    func_type = idaapi.tinfo_t()
    idaapi.get_tinfo(func_type, func_ea)
    idaapi.parse_decl(new_func_type, None, functio_proto, idaapi.PT_TYP)
    idaapi.apply_tinfo(func_ea, new_func_type, idaapi.TINFO_DEFINITE)
