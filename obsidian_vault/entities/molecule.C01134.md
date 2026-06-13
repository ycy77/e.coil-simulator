---
entity_id: "molecule.C01134"
entity_type: "small_molecule"
name: "Pantetheine 4'-phosphate"
source_database: "KEGG"
source_id: "C01134"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Pantetheine 4'-phosphate"
  - "4'-Phosphopantetheine"
  - "Phosphopantetheine"
  - "D-Pantetheine 4'-phosphate"
---

# Pantetheine 4'-phosphate

`molecule.C01134`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01134`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Pantetheine 4'-phosphate; 4'-Phosphopantetheine; Phosphopantetheine; D-Pantetheine 4'-phosphate EcoCyc common name: 4'-phosphopantetheine. PANTETHEINE-P "4'-Phosphopantetheine" is an essential prosthetic group of several acyl carrier proteins involved in pathways of primary and secondary metabolism. These include acyl carrier proteins (ACPs) of fatty acid synthases (FASs), ACPs of polyketide synthases (PKSs) and peptidyl carrier proteins (PCPs), and aryl carrier proteins of Non-ribosomal-peptide-synthetases "non-ribosomal peptide synthetases". The free thiol moiety of PANTETHEINE-P serves to covalently bind the acyl reaction intermediates as thioesters during the multistep assembly of the monomeric precursors, typically acetyl, malonyl, and aminoacyl groups . The PANTETHEINE-P moiety is derived from coenzyme A (CoA) and posttranslationally transferred onto an invariant serine side chain by EC-2.7.8.7, as described by this equation: HOLO-ACP-SYNTH-RXN Organisms often have several such enzymes; for example, TAX-562 have three enzymes, encoded by the EG10247, EG10262 and EG12221 genes.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 4 reaction(s). Binds entF (protein.P11454).

## Enriched Pathways

- `eco00332` Carbapenem biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Annotation

KEGG compound: Pantetheine 4'-phosphate; 4'-Phosphopantetheine; Phosphopantetheine; D-Pantetheine 4'-phosphate

## Pathways

- `eco00332` Carbapenem biosynthesis (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Outgoing Edges (6)

- `binds` --> [[protein.P11454|protein.P11454]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.ecocyc.2.3.1.49-RXN|reaction.ecocyc.2.3.1.49-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.3.1.4.14-RXN|reaction.ecocyc.3.1.4.14-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.P-PANTOCYSDECARB-RXN|reaction.ecocyc.P-PANTOCYSDECARB-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PANTETHEINE-KINASE-RXN|reaction.ecocyc.PANTETHEINE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.PANTEPADENYLYLTRAN-RXN|reaction.ecocyc.PANTEPADENYLYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01134`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
