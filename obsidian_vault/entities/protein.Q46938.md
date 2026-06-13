---
entity_id: "protein.Q46938"
entity_type: "protein"
name: "kduI"
source_database: "UniProt"
source_id: "Q46938"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kduI yqeE b2843 JW2811"
---

# kduI

`protein.Q46938`

## Static

- Type: `protein`
- Source: `UniProt:Q46938`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the isomerization of 5-dehydro-4-deoxy-D-glucuronate to 3-deoxy-D-glycero-2,5-hexodiulosonate (By similarity). Plays a role in the catabolism of hexuronates under osmotic stress conditions, likely substituting for the regular hexuronate degrading enzyme UxaC whose expression is repressed in these conditions (PubMed:23437267). {ECO:0000250|UniProtKB:Q05529, ECO:0000269|PubMed:23437267}. KduI was a predicted 5-keto 4-deoxyuronate isomerase due to its high sequence similarity to the enzyme from Erwinia chrysanthemi. In unpurified form, the enzyme appeares to be able to utilize both glucuronate and galacturonate, perhaps catalyzing the same reaction as UXAC-MONOMER "UxaC". While UxaC expression is repressed under osmotic stress conditions, KduI expression appears to be unaffected, and it could therefore substitute for UxaC . The purified protein was recently shown to catalyze the activity of EC-5.3.1.17 in coupled assays with KduD from Pectobacterium carotovorum or Streptococcus agalactiae . Based on its structural similarity to the Pyrococcus furiosus phosphoglucose isomerase, catalytic activity of KduI was tested with a panel of substrates; the enzyme showed activity with glucose-6-phosphate, glucuronate, and fructose-6-phosphate. The enzyme binds zinc, but catalytic activity is metal-independent . Crystal and solution structures of KduI have been solved...

## Biological Role

Component of 5-dehydro-4-deoxy-D-glucuronate isomerase (complex.ecocyc.CPLX-8401).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the isomerization of 5-dehydro-4-deoxy-D-glucuronate to 3-deoxy-D-glycero-2,5-hexodiulosonate (By similarity). Plays a role in the catabolism of hexuronates under osmotic stress conditions, likely substituting for the regular hexuronate degrading enzyme UxaC whose expression is repressed in these conditions (PubMed:23437267). {ECO:0000250|UniProtKB:Q05529, ECO:0000269|PubMed:23437267}.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-8401|complex.ecocyc.CPLX-8401]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2843|gene.b2843]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46938`
- `KEGG:ecj:JW2811;eco:b2843;ecoc:C3026_15610;`
- `GeneID:75203765;947319;`
- `GO:GO:0004347; GO:0005829; GO:0008270; GO:0008697; GO:0019698; GO:0042802; GO:0042803; GO:0042840; GO:0045490; GO:0046872`
- `EC:5.3.1.17`

## Notes

4-deoxy-L-threo-5-hexosulose-uronate ketol-isomerase (EC 5.3.1.17) (5-keto-4-deoxyuronate isomerase) (DKI isomerase)
