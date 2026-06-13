---
entity_id: "complex.ecocyc.ABC-62-CPLX"
entity_type: "complex"
name: "lipoprotein release complex"
source_database: "EcoCyc"
source_id: "ABC-62-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "LolCDE ABC transporter"
---

# lipoprotein release complex

`complex.ecocyc.ABC-62-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-62-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P75958|protein.P75958]], [[protein.P75957|protein.P75957]], [[protein.P0ADC3|protein.P0ADC3]]

## Enriched Summary

After post-translational modification (signal peptide cleavage and acylation) at the inner membrane, lipoproteins destined for the outer membrane in E. coli K-12 are exported via the 'lipoprotein outer membrane localization' pathway - the Lol pathway (reviewed in ). LolCDE is an essential inner membrane complex that mediates the release of lipoproteins from the periplasmic side of the inner membrane to the G6465-MONOMER "LolA" periplasmic chaperone. Purified LolCDE catalyses release of the outer membrane lipoproteins EG10684-MONOMER "Pal" and L10P (a derivative of EG10544-MONOMER "Lpp") from proteoliposomes in an in vitro system; a strain lacking LolCDE but carrying lolCDE on a temperature sensitive plasmid, is unable to grow at the non-permissive temperature and spheroplasts prepared from these cells have no lipoprotein releasing activity . Depletion of LolCDE results in the mislocalization of a model outer membrane lipoprotein to the inner membrane in vivo; the Pal lipoprotein remaining in spheroplasts upon depletion of LolBCD is sensitive to digestion by external proteinase K - this indicates that LolCDE depletion does not affect the translocation of lipoprotein across the inner membrane . LolCDE (unlike LolA and LolB) is fundamentally essential for lipoprotein trafficking; cpxA24 Δlpp ΔrcsB cells are highly sensitive to depletion of lolCDE...

## Biological Role

Catalyzes lipoprotein release (reaction.ecocyc.RXN-22427). Transports hν (molecule.ecocyc.Light).

## Annotation

After post-translational modification (signal peptide cleavage and acylation) at the inner membrane, lipoproteins destined for the outer membrane in E. coli K-12 are exported via the 'lipoprotein outer membrane localization' pathway - the Lol pathway (reviewed in ). LolCDE is an essential inner membrane complex that mediates the release of lipoproteins from the periplasmic side of the inner membrane to the G6465-MONOMER "LolA" periplasmic chaperone. Purified LolCDE catalyses release of the outer membrane lipoproteins EG10684-MONOMER "Pal" and L10P (a derivative of EG10544-MONOMER "Lpp") from proteoliposomes in an in vitro system; a strain lacking LolCDE but carrying lolCDE on a temperature sensitive plasmid, is unable to grow at the non-permissive temperature and spheroplasts prepared from these cells have no lipoprotein releasing activity . Depletion of LolCDE results in the mislocalization of a model outer membrane lipoprotein to the inner membrane in vivo; the Pal lipoprotein remaining in spheroplasts upon depletion of LolBCD is sensitive to digestion by external proteinase K - this indicates that LolCDE depletion does not affect the translocation of lipoprotein across the inner membrane . LolCDE (unlike LolA and LolB) is fundamentally essential for lipoprotein trafficking; cpxA24 Δlpp ΔrcsB cells are highly sensitive to depletion of lolCDE . The complex has a subunit stoichiometry of LolCLolD2LolE . The complex binds lipoproteins in a 1:1 stoichiometry . LolCDE and outer membrane specific lipoproteins (Pal, NlpC, YcfM, LolB) form tight complexes in the inner membrane and can be copurified in the absence of ATP; binding of lipoproteins to LolC/E increases the affinity of LolD for ATP; ATP hydrolysis and LolA are required for dissociation of an OM lipoprotein (Pal) fr

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-22427|reaction.ecocyc.RXN-22427]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0ADC3|protein.P0ADC3]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P75957|protein.P75957]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P75958|protein.P75958]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-62-CPLX`
- `PDB:7ARM`
- `PDB:7ARL`
- `PDB:7ARK`
- `PDB:7ARJ`
- `PDB:7ARI`
- `PDB:7ARH`
- `PDB:7V8M`
- `PDB:7V8L`
- `QSPROTEOME:QS00138383`

## Notes

1*protein.P75958|2*protein.P75957|1*protein.P0ADC3
