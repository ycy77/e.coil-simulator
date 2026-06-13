---
entity_id: "protein.P0A780"
entity_type: "protein"
name: "nusB"
source_database: "UniProt"
source_id: "P0A780"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nusB groNB ssyB b0416 JW0406"
---

# nusB

`protein.P0A780`

## Static

- Type: `protein`
- Source: `UniProt:P0A780`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Part of the processive rRNA transcription and antitermination complex (rrnTAC). The complex forms an RNA-chaperone ring around the RNA exit tunnel of RNA polymerase (RNAP). It supports rapid transcription and antitermination of rRNA operons, cotranscriptional rRNA folding, and annealing of distal rRNA regions to allow correct ribosome biogenesis (PubMed:32871103). Involved in transcription antitermination. Required for transcription of ribosomal RNA (rRNA) genes. Binds specifically to the boxA antiterminator sequence of the ribosomal RNA (rrn) operons (PubMed:11884128, PubMed:14973028, PubMed:15716433, PubMed:16109710, PubMed:7045592, PubMed:7678781). The affinity of NusB for the boxA RNA sequence is significantly increased in the presence of the ribosomal protein S10 (PubMed:11884128, PubMed:16109710). NusB may serve as a loading factor that ensures efficient entry of S10 into the transcription complexes (PubMed:19111659). It also modulates the rrn boxA-mediated transcription elongation rates (PubMed:10383769). {ECO:0000269|PubMed:10383769, ECO:0000269|PubMed:11884128, ECO:0000269|PubMed:14973028, ECO:0000269|PubMed:15716433, ECO:0000269|PubMed:16109710, ECO:0000269|PubMed:19111659, ECO:0000269|PubMed:32871103, ECO:0000269|PubMed:7045592, ECO:0000269|PubMed:7678781}...

## Biological Role

Component of NusB-S10 complex (complex.ecocyc.CPLX0-7879).

## Annotation

FUNCTION: Part of the processive rRNA transcription and antitermination complex (rrnTAC). The complex forms an RNA-chaperone ring around the RNA exit tunnel of RNA polymerase (RNAP). It supports rapid transcription and antitermination of rRNA operons, cotranscriptional rRNA folding, and annealing of distal rRNA regions to allow correct ribosome biogenesis (PubMed:32871103). Involved in transcription antitermination. Required for transcription of ribosomal RNA (rRNA) genes. Binds specifically to the boxA antiterminator sequence of the ribosomal RNA (rrn) operons (PubMed:11884128, PubMed:14973028, PubMed:15716433, PubMed:16109710, PubMed:7045592, PubMed:7678781). The affinity of NusB for the boxA RNA sequence is significantly increased in the presence of the ribosomal protein S10 (PubMed:11884128, PubMed:16109710). NusB may serve as a loading factor that ensures efficient entry of S10 into the transcription complexes (PubMed:19111659). It also modulates the rrn boxA-mediated transcription elongation rates (PubMed:10383769). {ECO:0000269|PubMed:10383769, ECO:0000269|PubMed:11884128, ECO:0000269|PubMed:14973028, ECO:0000269|PubMed:15716433, ECO:0000269|PubMed:16109710, ECO:0000269|PubMed:19111659, ECO:0000269|PubMed:32871103, ECO:0000269|PubMed:7045592, ECO:0000269|PubMed:7678781}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7879|complex.ecocyc.CPLX0-7879]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0416|gene.b0416]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A780`
- `KEGG:ecj:JW0406;eco:b0416;ecoc:C3026_02030;`
- `GeneID:86862961;93777044;945054;`
- `GO:GO:0003723; GO:0005829; GO:0006353; GO:0008023; GO:0031564; GO:0032784; GO:0042254`

## Notes

Transcription antitermination protein NusB (Antitermination factor NusB) (N utilization substance protein B)
