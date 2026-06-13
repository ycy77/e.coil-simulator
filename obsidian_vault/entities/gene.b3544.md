---
entity_id: "gene.b3544"
entity_type: "gene"
name: "dppA"
source_database: "NCBI RefSeq"
source_id: "gene-b3544"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3544"
  - "dppA"
---

# dppA

`gene.b3544`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3544`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dppA (gene.b3544) is a gene entity. It encodes dppA (protein.P23847). Encoded protein function: FUNCTION: Part of the ABC transporter DppABCDF involved in dipeptide transport (PubMed:10537211, PubMed:1702779, PubMed:7536291). Binds dipeptides and accepts a wide range of side chains, including small neutral, bulky hydrophobic, and positively and negatively charged groups (PubMed:10537211). Tripeptides are poor substrates (PubMed:10537211). DppA alone controls the specificity of the Dpp transporter (PubMed:10537211). In addition, plays a role in chemotaxis toward peptides via interaction with the chemotaxis protein Tap (PubMed:3520334, PubMed:8563629). {ECO:0000269|PubMed:10537211, ECO:0000269|PubMed:1702779, ECO:0000269|PubMed:3520334, ECO:0000269|PubMed:7536291, ECO:0000269|PubMed:8563629}.; FUNCTION: Binds heme. When a foreign outer membrane heme receptor is expressed in E.coli, DppABCDF can also transport heme and its precursor, 5-aminolevulinic acid (ALA), from the periplasm into the cytoplasm. {ECO:0000269|PubMed:16905647, ECO:0000269|PubMed:8444807}. EcoCyc product frame: DPPA-MONOMER. EcoCyc synonyms: alu, dpp, fpp. Genomic coordinates: 3706098-3707705. EcoCyc protein note: DppA is the periplasmic binding protein of a dipeptide ABC transport system...

## Biological Role

Repressed by lrp (protein.P0ACJ0), nac (protein.Q47005). Activated by rpoD (protein.P00579), arcA (protein.P0A9Q1), lrp (protein.P0ACJ0), nac (protein.Q47005).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23847|protein.P23847]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=dppA; function=+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=dppA; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=dppA; function=-+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=dppA; function=-+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011576,ECOCYC:EG10248,GeneID:948062`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3706098-3707705:-; feature_type=gene
