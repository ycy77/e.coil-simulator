---
entity_id: "protein.P0ADY3"
entity_type: "protein"
name: "rplN"
source_database: "UniProt"
source_id: "P0ADY3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rplN b3310 JW3272"
---

# rplN

`protein.P0ADY3`

## Static

- Type: `protein`
- Source: `UniProt:P0ADY3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Binds to 23S rRNA. Forms part of two intersubunit bridges in the 70S ribosome. {ECO:0000255|HAMAP-Rule:MF_01367}.; FUNCTION: In the 3.5 A resolved structures L14 and L19 interact and together make contact with the 16S rRNA in bridges B5 and B8 (PubMed:12809609, PubMed:16272117). {ECO:0000269|PubMed:12809609, ECO:0000269|PubMed:16272117}.; FUNCTION: Can interact with RsfS, in this case bridge B8 probably cannot form, and the 30S and 50S ribosomal subunits do not associate, which represses translation (PubMed:22829778, PubMed:33639093). {ECO:0000269|PubMed:22829778, ECO:0000269|PubMed:33639093}. The L14 protein is a component of the 50S subunit of the ribosome. L14 crosslinks to 23S rRNA . In the cryo-EM reconstruction of the ribosome, L14 was modelled to be located at the 30S-50S subunit interface, at bridges B5 and B8 . In all-atom molecular dynamics simulations of the ribosome, a structural gate between helices 71 and 92 of 23S rRNA restricts tRNA motion and together with L14 acts as a steric filter for the cognate tRNA . L14 interacts directly with EG11255-MONOMER. Amino acid residues in L14 that are essential for this interaction have been identified by mutagenesis . Based on amino-terminal sequencing of the purified protein, L14 may be identical to Rep helicase stimulatory protein (RHSP) . RHSP forms aggregates on DNA and interacts with rRNA...

## Biological Role

Component of 50S ribosomal subunit (complex.ecocyc.CPLX0-3962).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: Binds to 23S rRNA. Forms part of two intersubunit bridges in the 70S ribosome. {ECO:0000255|HAMAP-Rule:MF_01367}.; FUNCTION: In the 3.5 A resolved structures L14 and L19 interact and together make contact with the 16S rRNA in bridges B5 and B8 (PubMed:12809609, PubMed:16272117). {ECO:0000269|PubMed:12809609, ECO:0000269|PubMed:16272117}.; FUNCTION: Can interact with RsfS, in this case bridge B8 probably cannot form, and the 30S and 50S ribosomal subunits do not associate, which represses translation (PubMed:22829778, PubMed:33639093). {ECO:0000269|PubMed:22829778, ECO:0000269|PubMed:33639093}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3962|complex.ecocyc.CPLX0-3962]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b3310|gene.b3310]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADY3`
- `KEGG:ecj:JW3272;eco:b3310;ecoc:C3026_17990;`
- `GeneID:86862292;93778677;947809;`
- `GO:GO:0002181; GO:0003735; GO:0005737; GO:0005829; GO:0022625; GO:0070180`

## Notes

Large ribosomal subunit protein uL14 (50S ribosomal protein L14)
