---
entity_id: "gene.b4599"
entity_type: "gene"
name: "mgtS"
source_database: "NCBI RefSeq"
source_id: "gene-b4599"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4599"
  - "mgtS"
---

# mgtS

`gene.b4599`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4599`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mgtS (gene.b4599) is a gene entity. It encodes mgtS (protein.A5A616). Encoded protein function: FUNCTION: Modulates intracellular Mg(2+) levels to maintain cellular integrity upon Mg(2+) limitation. Acts by binding and stabilizing the Mg(2+) transporter MgtA, thereby leading to increased intracellular level of Mg(2+). May inhibit FtsH proteolysis of MgtA. {ECO:0000269|PubMed:28512220}. EcoCyc product frame: MONOMER0-766. EcoCyc synonyms: yneM. Genomic coordinates: 1622646-1622741. EcoCyc protein note: MgtS is a small, inner membrane protein which interacts with the Mg2+ transporter, MGTA-MONOMER "MgtA" and the PITA-MONOMER "PitA low-affinity phosphate transporter" to promote intracellular Mg2+ accumulation; the interactions are implicated in regulatory cross-talk between Mg2+ and phosphate homeostasis When grown under Mg2+ limitation and compared to the wild-type, a ΔmgtS mutant has lower intracellular Mg2+ levels and displays a growth defect; MgtS and MgtA co-purify in a reciprocal manner . MgtA accumulates normally in a ΔmgtS strain that overexpresses a known FtsH substrate (phage lambda cII protein), indicating that MgtS may act to stabilize MgtA by inhibiting FtsH proteolysis of MgtA...

## Biological Role

Activated by rpoD (protein.P00579), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.A5A616|protein.A5A616]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mgtS; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=mgtS; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ECOCYC:G0-8892,GeneID:5061497`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1622646-1622741:+; feature_type=gene
