from sqlite3 import InternalError
import nextcord

class RoleView(nextcord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def click_handler(self, button: nextcord.ui.Button, interaction: nextcord.Interaction, role_id: int):
        role  = interaction.guild.get_role(role_id)
        assert isinstance(role, nextcord.Role)

        if role not in interaction.user.roles:
            await interaction.user.add_roles(role)
            await interaction.response.send_message('add role successfully', ephemeral=True)
        else:
            await interaction.user.remove_roles(role)

            await interaction.response.send_message('remove role successfully', ephemeral=True)

    @nextcord.ui.button(label='test_role1', emoji='🥴', style=nextcord.ButtonStyle.primary, custom_id=str(hash('RoleView' + 'test_role1')))
    async def test_role1_button(self, button, interaction):
        # await interaction.response.send_message('you choose test_role1', ephemeral=True)
        await self.click_handler(button=button, interaction=interaction, role_id=999665564857409596)


    @nextcord.ui.button(label='test_role2', emoji= '😄', style=nextcord.ButtonStyle.primary, custom_id=str(hash('RoleView' + 'test_role2')))
    async def test_role2_button(self, button: nextcord.ui.Button, interaction: nextcord.Interaction): #todo is the type of button correct?
        # await interaction.response.send_message('you choose test_role2', ephemeral=True)
        await self.click_handler(button=button, interaction=interaction, role_id=999665732415651860)