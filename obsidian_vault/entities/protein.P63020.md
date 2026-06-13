---
entity_id: "protein.P63020"
entity_type: "protein"
name: "nfuA"
source_database: "UniProt"
source_id: "P63020"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nfuA gntY yhgI b3414 JW3377"
---

# nfuA

`protein.P63020`

## Static

- Type: `protein`
- Source: `UniProt:P63020`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in iron-sulfur cluster biogenesis under severe conditions such as iron starvation or oxidative stress. Binds a 4Fe-4S cluster, can transfer this cluster to apoproteins, and thereby intervenes in the maturation of Fe/S proteins. Could also act as a scaffold/chaperone for damaged Fe/S proteins. Required for E.coli to sustain oxidative stress and iron starvation. Also necessary for the use of extracellular DNA as the sole source of carbon and energy. {ECO:0000269|PubMed:16707682, ECO:0000269|PubMed:18339628}. NfuA is a 'non-ISC, non-SUF' iron-sulfur (Fe-S) cluster carrier protein. NfuA can receive Fe-S clusters from the SufBC2D and IscU/HscBA scaffold-containing complexes and can in turn transfer Fe-S clusters to the A-type carrier proteins EG11378-MONOMER SufA and EG12132-MONOMER IscA . NfuA is able to transfer its iron-sulfur cluster to ACONITASE-MONOMER apo-AcnA and ACONITATEDEHYDRB-MONOMER apo-AcnB and appears to be involved in the maturation of EG12087 NuoG, an iron-sulfur cluster-containing subunit of NADH dehydrogenase I . Both NfuA and EG12181-MONOMER "GrxD" interact with G6364-MONOMER "MiaB". NfuA, but not GrxD, can transfer a 4Fe-4S cluster to apo-MiaB in vitro, and both proteins affect MiaB activity in vivo...

## Biological Role

Component of [Fe-S] cluster carrier protein NfuA (complex.ecocyc.CPLX0-7682).

## Annotation

FUNCTION: Involved in iron-sulfur cluster biogenesis under severe conditions such as iron starvation or oxidative stress. Binds a 4Fe-4S cluster, can transfer this cluster to apoproteins, and thereby intervenes in the maturation of Fe/S proteins. Could also act as a scaffold/chaperone for damaged Fe/S proteins. Required for E.coli to sustain oxidative stress and iron starvation. Also necessary for the use of extracellular DNA as the sole source of carbon and energy. {ECO:0000269|PubMed:16707682, ECO:0000269|PubMed:18339628}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7682|complex.ecocyc.CPLX0-7682]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3414|gene.b3414]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P63020`
- `KEGG:ecj:JW3377;eco:b3414;ecoc:C3026_18520;`
- `GeneID:86862187;93778582;947925;`
- `GO:GO:0005506; GO:0005829; GO:0006979; GO:0010106; GO:0015976; GO:0016226; GO:0042803; GO:0051539; GO:0051604; GO:0140132`

## Notes

Fe/S biogenesis protein NfuA
