---
entity_id: "molecule.C00120"
entity_type: "small_molecule"
name: "Biotin"
source_database: "KEGG"
source_id: "C00120"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Biotin"
  - "D-Biotin"
  - "Vitamin H"
  - "Coenzyme R"
---

# Biotin

`molecule.C00120`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00120`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Biotin; D-Biotin; Vitamin H; Coenzyme R BIOTIN "Biotin" is a water soluble, heterocyclic cofactor for a small number of enzymes that facilitate the transfer of CO2 during carboxylation, decarboxylation and transcarboxylation reactions involved in fatty acid and carbohydrate metabolism . The biotin-requiring enzymes identified so far (including ACETYL-COA-CARBOXYLMULTI-CPLX, CPLX66-17, CPLX-5203, and CPLX-6001) play essential roles in cell metabolism . Humans and other mammals cannot synthesize biotin and thus must obtain it from exogenous sources via intestinal absorption. Biotin was first discovered at the turn of the 20th century as a yeast growth factor, and was named bios . 30 years later, the compound was purified from egg yolk by Koegl and Toennis . In a completely unrelated research, Gyoergy and his colleagues discovered biotin in liver in 1931, and isolated it in 1941. They named it vitamin H (for the German word for skin: Haut) . At the same time, another group, which was working on Rhizobia bacteria, also identified it as an essential cofactor, which they named coenzyme R . Already in 1933, Gyoergy suggested that coenzyme R, bios and vitamin H were all the same molecule. The structure of biotin was solved in 1941 -1942...

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 3 reaction(s). Binds PROPIONYL-COA-CARBOXY-MONOMER (protein.ecocyc.PROPIONYL-COA-CARBOXY-MONOMER).

## Enriched Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Biotin; D-Biotin; Vitamin H; Coenzyme R

## Pathways

- `eco00780` Biotin metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (8)

- `binds` --> [[protein.ecocyc.PROPIONYL-COA-CARBOXY-MONOMER|protein.ecocyc.PROPIONYL-COA-CARBOXY-MONOMER]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.ecocyc.RXN-17473|reaction.ecocyc.RXN-17473]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6277|reaction.ecocyc.RXN0-6277]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-240|reaction.ecocyc.TRANS-RXN0-240]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.BIOTINLIG-RXN|reaction.ecocyc.BIOTINLIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7192|reaction.ecocyc.RXN0-7192]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-240|reaction.ecocyc.TRANS-RXN0-240]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.BIOTIN-CARBOXYL-RXN|reaction.ecocyc.BIOTIN-CARBOXYL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00120`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
