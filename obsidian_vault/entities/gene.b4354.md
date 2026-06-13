---
entity_id: "gene.b4354"
entity_type: "gene"
name: "btsT"
source_database: "NCBI RefSeq"
source_id: "gene-b4354"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4354"
  - "btsT"
---

# btsT

`gene.b4354`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4354`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

btsT (gene.b4354) is a gene entity. It encodes btsT (protein.P39396). Encoded protein function: FUNCTION: Transports pyruvate with a high affinity and specificity. The process is driven by the proton motive force (PubMed:29061664). Under nutrient limiting conditions, mediates the uptake of pyruvate, thus enabling it to be used as a carbon source for the growth and survival (PubMed:29061664). Part of a nutrient-sensing regulatory network composed of the two-component regulatory systems BtsS/BtsR and YpdA/YpdB, and their respective target proteins, BtsT and YhjX (PubMed:24659770). {ECO:0000269|PubMed:24659770, ECO:0000269|PubMed:29061664}. EcoCyc product frame: G7942-MONOMER. EcoCyc synonyms: yjiY. Genomic coordinates: 4589129-4591279. EcoCyc protein note: BtsT is a high-affinity, pyruvate:H+ symporter which mediates the uptake of pyruvate under nutrient limiting conditions. Extrachromosomal expression of btsT in a ΔbtsT mutant and in a strain with decreased pyruvate metabolism increases the uptake rate of labeled pyruvate compared to the control; transport is highest at pH 7.5, decreases at pH 6 and is not detected at pH 4.5 and 3; transport is abolished upon addition of the protonophores 2,4-dinitro-phenol (DNP) or carbonyl cyanide m-chlorophenyl hydrazone (CCCP)...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748). Activated by crp (protein.P0ACJ8), btsR (protein.P0AFT5), rpoS (protein.P13445).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39396|protein.P39396]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=btsT; function=+
- `activates` <-- [[protein.P0AFT5|protein.P0AFT5]] `RegulonDB` `C` - regulator=BtsR; target=btsT; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=btsT; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0014278,ECOCYC:G7942,GeneID:948914`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4589129-4591279:-; feature_type=gene
