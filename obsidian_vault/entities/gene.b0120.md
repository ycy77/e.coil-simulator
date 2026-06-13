---
entity_id: "gene.b0120"
entity_type: "gene"
name: "speD"
source_database: "NCBI RefSeq"
source_id: "gene-b0120"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0120"
  - "speD"
---

# speD

`gene.b0120`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0120`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

speD (gene.b0120) is a gene entity. It encodes speD (protein.P0A7F6). Encoded protein function: FUNCTION: Catalyzes the decarboxylation of S-adenosylmethionine to S-adenosylmethioninamine (dcAdoMet), the propylamine donor required for the synthesis of the polyamines spermine and spermidine from the diamine putrescine. EcoCyc product frame: SPED-MONOMER. Genomic coordinates: 134788-135582. EcoCyc protein note: S-adenosylmethionine (AdoMet) decarboxylase (SpeD) is an important enzyme of polyamine biosynthesis in all domains of life. It catalyzes the removal of the carboxylate group of S-adenosyl-L-methionine, producing S-adenosyl-L-methioninamine. This compound then acts as the n-propylamine group donor for the synthesis of spermidine from putrescine by SPERMIDINESYN-CPLX. Inhibition of AdoMet decarboxylase by spermidine appears to be the most significant physiological regulator of polyamine biosynthesis, probably limiting it when the intracellular spermidine concentration becomes excessive . This enzyme belongs to a small class of decarboxylating enzymes that utilize covalently bound pyruvate (pyruvoyl group). Class 1 enzymes are found in bacteria and archaea, while Class 2 are found in eukaryotes. These two classes show almost no detectable sequence homology with each other and do not show similarity to other known pyruvoyl-dependent amino acid decarboxylases...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7F6|protein.P0A7F6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=speD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000416,ECOCYC:EG10962,GeneID:947719`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:134788-135582:-; feature_type=gene
