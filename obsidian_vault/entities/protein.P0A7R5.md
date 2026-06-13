---
entity_id: "protein.P0A7R5"
entity_type: "protein"
name: "rpsJ"
source_database: "UniProt"
source_id: "P0A7R5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpsJ nusE b3321 JW3283"
---

# rpsJ

`protein.P0A7R5`

## Static

- Type: `protein`
- Source: `UniProt:P0A7R5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the binding of tRNA to the ribosomes (PubMed:6759118). Part of the processive rRNA transcription and antitermination complex (rrnTAC). The complex forms an RNA-chaperone ring around the RNA exit tunnel of RNA polymerase (RNAP). It supports rapid transcription and antitermination of rRNA operons, cotranscriptional rRNA folding, and annealing of distal rRNA regions to allow correct ribosome biogenesis (PubMed:32871103). In complex with NusB is involved in the regulation of ribosomal RNA (rRNA) biosynthesis by transcriptional antitermination. S10 binds RNA non-specifically and increases the affinity of NusB for the boxA RNA sequence (PubMed:11884128, PubMed:16109710, PubMed:7678781). S10 may constitute the critical antitermination component of the NusB-S10 complex (PubMed:19111659). {ECO:0000269|PubMed:11884128, ECO:0000269|PubMed:16109710, ECO:0000269|PubMed:19111659, ECO:0000269|PubMed:32871103, ECO:0000269|PubMed:6759118, ECO:0000269|PubMed:7678781}. The S10 protein (NusE) is a component of the 30S subunit of the ribosome. From within its location in the ribosome, S10 plays a role in linking transcription and translation; in a separate complex with NusB, it plays a role in regulating transcription antitermination. S10 can be crosslinked to tRNA in the ribosomal P site and may contact 16S rRNA in two separate domains...

## Biological Role

Component of 30S ribosomal subunit (complex.ecocyc.CPLX0-3953), NusB-S10 complex (complex.ecocyc.CPLX0-7879).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: Involved in the binding of tRNA to the ribosomes (PubMed:6759118). Part of the processive rRNA transcription and antitermination complex (rrnTAC). The complex forms an RNA-chaperone ring around the RNA exit tunnel of RNA polymerase (RNAP). It supports rapid transcription and antitermination of rRNA operons, cotranscriptional rRNA folding, and annealing of distal rRNA regions to allow correct ribosome biogenesis (PubMed:32871103). In complex with NusB is involved in the regulation of ribosomal RNA (rRNA) biosynthesis by transcriptional antitermination. S10 binds RNA non-specifically and increases the affinity of NusB for the boxA RNA sequence (PubMed:11884128, PubMed:16109710, PubMed:7678781). S10 may constitute the critical antitermination component of the NusB-S10 complex (PubMed:19111659). {ECO:0000269|PubMed:11884128, ECO:0000269|PubMed:16109710, ECO:0000269|PubMed:19111659, ECO:0000269|PubMed:32871103, ECO:0000269|PubMed:6759118, ECO:0000269|PubMed:7678781}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3953|complex.ecocyc.CPLX0-3953]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-7879|complex.ecocyc.CPLX0-7879]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3321|gene.b3321]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7R5`
- `KEGG:ecj:JW3283;eco:b3321;ecoc:C3026_18045;`
- `GeneID:86862281;93778666;947816;`
- `GO:GO:0000049; GO:0001072; GO:0002181; GO:0003735; GO:0005737; GO:0005829; GO:0008023; GO:0015935; GO:0022627; GO:0031564; GO:0032784; GO:0042254`

## Notes

Small ribosomal subunit protein uS10 (30S ribosomal protein S10) (Transcription termination/antitermination protein NusE)
