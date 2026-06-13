---
entity_id: "complex.ecocyc.CPLX0-248"
entity_type: "complex"
name: "cysteine desulfurase IscS"
source_database: "EcoCyc"
source_id: "CPLX0-248"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# cysteine desulfurase IscS

`complex.ecocyc.CPLX0-248`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-248`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A6B7|protein.P0A6B7]]

## Enriched Summary

Cysteine desulfurase (IscS) catalyzes the transfer of sulfur and selenium from cysteine and selenocysteine to a range of recipients. It is critical for addition of sulfur to tRNA, for synthesis and repair of iron-sulfur (Fe-S) clusters, for synthesis of molybdopterin cofactors, and for generation of a number of other sulfur- and selenium-dependent proteins. IscS is a PYRIDOXAL_PHOSPHATE (PLP)-dependent cysteine desulfurase that catalyzes the conversion of cysteine into alanine and sulfur via intermediate formation of a cysteine persulfide on Cys328. Although the mechanism appears to differ for selenium, IscS can similarly convert L-selenocysteine to alanine . IscS is one of three members of the NifS protein family in E. coli, the other two being CPLX0-246 and CPLX0-7838 . IscS provides sulfur and selenium for modification of several positions on a number of tRNAs, and is responsible for 95% of all sulfur in cellular tRNA . Donation of sulfur for 4-thiouridine in tRNA occurs via transfer to the intermediate protein, THII-MONOMER . Another intermediate protein, EG11344 MnmA, is similarly required for IscS-dependent 2-thiouridine biosynthesis . 2-thiouridine synthesis at tRNA wobble sites requires EG12216 TusA, a protein that activates IscS desulfurase activity and accepts activated sulfur from it as a cysteine persulfide...

## Biological Role

Catalyzes RXN-12587 (reaction.ecocyc.RXN-12587), RXN-12588 (reaction.ecocyc.RXN-12588), RXN-14382 (reaction.ecocyc.RXN-14382), RXN-21566 (reaction.ecocyc.RXN-21566), RXN-22698 (reaction.ecocyc.RXN-22698), RXN-22700 (reaction.ecocyc.RXN-22700), RXN-25085 (reaction.ecocyc.RXN-25085), cysteine:[ThiI sulfur-carrier protein]-L-cysteine sulfurtransferase desulfurase (reaction.ecocyc.RXN-9787), and 1 more. Component of IscS:TusA sulfurtransferase (complex.ecocyc.CPLX0-12610). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

Cysteine desulfurase (IscS) catalyzes the transfer of sulfur and selenium from cysteine and selenocysteine to a range of recipients. It is critical for addition of sulfur to tRNA, for synthesis and repair of iron-sulfur (Fe-S) clusters, for synthesis of molybdopterin cofactors, and for generation of a number of other sulfur- and selenium-dependent proteins. IscS is a PYRIDOXAL_PHOSPHATE (PLP)-dependent cysteine desulfurase that catalyzes the conversion of cysteine into alanine and sulfur via intermediate formation of a cysteine persulfide on Cys328. Although the mechanism appears to differ for selenium, IscS can similarly convert L-selenocysteine to alanine . IscS is one of three members of the NifS protein family in E. coli, the other two being CPLX0-246 and CPLX0-7838 . IscS provides sulfur and selenium for modification of several positions on a number of tRNAs, and is responsible for 95% of all sulfur in cellular tRNA . Donation of sulfur for 4-thiouridine in tRNA occurs via transfer to the intermediate protein, THII-MONOMER . Another intermediate protein, EG11344 MnmA, is similarly required for IscS-dependent 2-thiouridine biosynthesis . 2-thiouridine synthesis at tRNA wobble sites requires EG12216 TusA, a protein that activates IscS desulfurase activity and accepts activated sulfur from it as a cysteine persulfide . No intermediate protein has yet been identified for the IscS-dependent synthesis of 2-selenouridines on tRNA . In addition to its role in tRNA modification, IscS is critical for iron-sulfur (Fe-S) cluster formation and repair . IscS transfers sulfur to the coregulated "scaffold" protein G7324 IscU, on which Fe-S clusters are assembled . The two proteins form a disulfide linkage between Cys-63 of IscU and Cys-328 of IscS. This interaction between IscU an

## Outgoing Edges (11)

- `activates` --> [[reaction.ecocyc.TRNA-S-TRANSFERASE-RXN|reaction.ecocyc.TRNA-S-TRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `catalyzes` --> [[reaction.ecocyc.RXN-12587|reaction.ecocyc.RXN-12587]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-12588|reaction.ecocyc.RXN-12588]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-14382|reaction.ecocyc.RXN-14382]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-21566|reaction.ecocyc.RXN-21566]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-22698|reaction.ecocyc.RXN-22698]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-22700|reaction.ecocyc.RXN-22700]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-25085|reaction.ecocyc.RXN-25085]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-9787|reaction.ecocyc.RXN-9787]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-308|reaction.ecocyc.RXN0-308]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-12610|complex.ecocyc.CPLX0-12610]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0A6B7|protein.P0A6B7]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-248`
- `QSPROTEOME:QS00093492`

## Notes

2*protein.P0A6B7
