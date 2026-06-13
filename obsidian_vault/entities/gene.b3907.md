---
entity_id: "gene.b3907"
entity_type: "gene"
name: "rhaT"
source_database: "NCBI RefSeq"
source_id: "gene-b3907"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3907"
  - "rhaT"
---

# rhaT

`gene.b3907`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3907`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rhaT (gene.b3907) is a gene entity. It encodes rhaT (protein.P27125). Encoded protein function: FUNCTION: Uptake of L-rhamnose across the cytoplasmic membrane with the concomitant transport of protons into the cell (symport system) (PubMed:1551902, PubMed:2283027, PubMed:8384447). Can also transport L-mannose and L-lyxose, but at reduced rates (PubMed:1650346, PubMed:8384447). {ECO:0000269|PubMed:1551902, ECO:0000269|PubMed:1650346, ECO:0000269|PubMed:2283027, ECO:0000269|PubMed:8384447}. EcoCyc product frame: RHAT-MONOMER. Genomic coordinates: 4099491-4100525. EcoCyc protein note: RhaT is the sole transporter for rhamnose in E. coli and functions as a rhamnose/proton symporter. rhaT mutants were unable to utilise or transport rhamnose, and this defect could be complemented by the cloned rhaT gene . Studies in membrane vesicles have shown that RhaT can transport rhamnose with moderate affinity (20-40 μM) and that rhamnose transport is coupled with proton transport . RhaT is also able to transport L-lyxose . RhaT is the prototype member of the RhaT family of transporters. Analysis of RhaT-BlaZ fusions has indicated that the RhaT protein contains 10 transmembrane segments . Expression of rhaT is induced by rhamnose in a process involving RhaS and RhaT . An inhibitory effect on rhaT induced by rhamnose appears in the presence of a higher concentration of arabinose or xylose .

## Biological Role

Activated by rpoD (protein.P00579), rhaS (protein.P09377).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P27125|protein.P27125]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rhaT; function=+
- `activates` <-- [[protein.P09377|protein.P09377]] `RegulonDB` `S` - regulator=RhaS; target=rhaT; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012749,ECOCYC:EG11313,GeneID:948398`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4099491-4100525:-; feature_type=gene
