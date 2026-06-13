---
entity_id: "protein.P0A948"
entity_type: "protein"
name: "rimJ"
source_database: "UniProt"
source_id: "P0A948"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rimJ b1066 JW1053"
---

# rimJ

`protein.P0A948`

## Static

- Type: `protein`
- Source: `UniProt:P0A948`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Acetylates the N-terminal alanine of ribosomal protein uS5 (PubMed:2828880, PubMed:385889). Also plays a role in maturation of the 30S ribosomal subunit (PubMed:18466225, PubMed:20176963). Plays a role in the temperature regulation of pap pilin transcription (PubMed:1356970). {ECO:0000269|PubMed:1356970, ECO:0000269|PubMed:18466225, ECO:0000269|PubMed:20176963, ECO:0000269|PubMed:2828880, ECO:0000269|PubMed:385889}. RimJ is an alanine acetyltransferase that is specific for EG10904-MONOMER . RimJ also plays a role in maturation of the 30S ribosomal subunit . RimJ interacts with pre-30S, but not mature ribosomal subunits . RimJ has overall similarity to RimL and C-terminal similarity to RimI . Overexpression of RimJ, even when lacking its acetyltransferase activity, suppresses the 16S rRNA maturation defect of an RpsE G28D mutant . Overexpression of RimJ decreases the levels of the immature long precursor 16S rRNA (lp16S rRNA) in the RpsE G28D mutant . In a rimJ mutant, the ribosomal protein S5 is not acetylated at the N terminus . Mutation of the conserved cysteine residues C54 and/or C105 results in loss of RimJ acetyltransferase activity . RimJ acts in transcriptional regulation of the pap pilin operon by environmental conditions in uropathogenic E. coli . Tcp: "thermoregulatory control of pap" RimJ: "ribosomal modification J" Review:

## Biological Role

Catalyzes RXN-18434 (reaction.ecocyc.RXN-18434).

## Annotation

FUNCTION: Acetylates the N-terminal alanine of ribosomal protein uS5 (PubMed:2828880, PubMed:385889). Also plays a role in maturation of the 30S ribosomal subunit (PubMed:18466225, PubMed:20176963). Plays a role in the temperature regulation of pap pilin transcription (PubMed:1356970). {ECO:0000269|PubMed:1356970, ECO:0000269|PubMed:18466225, ECO:0000269|PubMed:20176963, ECO:0000269|PubMed:2828880, ECO:0000269|PubMed:385889}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-18434|reaction.ecocyc.RXN-18434]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1066|gene.b1066]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A948`
- `KEGG:ecj:JW1053;eco:b1066;ecoc:C3026_06475;`
- `GeneID:89515939;93776341;946910;`
- `GO:GO:0005737; GO:0005829; GO:0008080; GO:0008999; GO:0030490; GO:0042254; GO:1990189`
- `EC:2.3.1.267`

## Notes

[Ribosomal protein uS5]-alanine N-acetyltransferase (EC 2.3.1.267) (Acetylating enzyme for N-terminal of ribosomal protein S5)
