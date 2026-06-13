---
entity_id: "gene.b0598"
entity_type: "gene"
name: "cstA"
source_database: "NCBI RefSeq"
source_id: "gene-b0598"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0598"
  - "cstA"
---

# cstA

`gene.b0598`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0598`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cstA (gene.b0598) is a gene entity. It encodes cstA (protein.P15078). Encoded protein function: FUNCTION: Involved in peptide utilization during carbon starvation. {ECO:0000269|PubMed:1848300}. EcoCyc product frame: EG10167-MONOMER. EcoCyc synonyms: ybdC. Genomic coordinates: 629894-631999. EcoCyc protein note: cstA encodes a specific, moderate affinity pyruvate transporter which mediates the proton-dependent uptake of pyruvate; expression of the transporter from a plasmid enables the growth of a triple mutant strain (ΔG7942 btsT ΔcstA ΔEG12268 yhjX) that is otherwise unable to grow with pyruvate as a sole carbon and energy source . cstA is induced during carbon (succinate, glycerol or glucose) starvation or upon entry into stationary phase; expression is dependent on RPOD-MONOMER σ70 and positively regulated by cAMP-CRP . The growth impairment of cstA opp double null mutants is evident only when peptides serve as carbon and energy source implicating cstA in peptide utilization . cstA expression is negatively regulated by CPLX0-7705 Fis and by CPLX0-7956 CsrA; CsrA binds specifically to cstA mRNA and the interaction is highly cooperative...

## Biological Role

Repressed by gcvB (gene.b4443). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15078|protein.P15078]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cstA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=cstA; function=+
- `represses` <-- [[gene.b4443|gene.b4443]] `RegulonDB` `S` - regulator=GcvB; target=cstA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002061,ECOCYC:EG10167,GeneID:945213`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:629894-631999:+; feature_type=gene
