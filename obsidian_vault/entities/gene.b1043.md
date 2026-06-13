---
entity_id: "gene.b1043"
entity_type: "gene"
name: "csgC"
source_database: "NCBI RefSeq"
source_id: "gene-b1043"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1043"
  - "csgC"
---

# csgC

`gene.b1043`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1043`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

csgC (gene.b1043) is a gene entity. It encodes csgC (protein.P52107). Encoded protein function: FUNCTION: Plays a role in the extracellular assembly of CsgA into thin aggregative fimbriae (Tafi) fibers. Assembly may also require CsgE. Tafi are thought to be assembled via an extracellular nucleation-precipitation (ENP) pathway, and possibly also via an intracellular non-CsgC-dependent pathway (By similarity). {ECO:0000250}. EcoCyc product frame: G6548-MONOMER. EcoCyc synonyms: ycdE. Genomic coordinates: 1104961-1105293. EcoCyc protein note: CsgC is a periplasmic chaperone that maintains the curlin subunit, EG11489-MONOMER "CsgA", in a soluble monomeric state. Genetic and biochemical analyses suggest that CsgC has anti-amyloid activity. Purified CsgC inhibits CsgA polymerization in vitro; in the presence of CsgC, CsgA remains unfolded and non-amyloidogenic; CsgC prevents CsgA from adopting β sheet containing structures . CsgC (from an unspecified E. coli strain) has been purified and crystallised. It consists of 7 β strands forming 2 β sheets; it exhibits structural similarity with the N-terminal domain of DSBD-MONOMER "DsbD disulfide oxidoreductase" An insertion in csgC does not affect production of curli, but abolishes the autoagglutinating ability which curliated cells normally possess...

## Biological Role

Repressed by btsR (protein.P0AFT5). Activated by FlhDC DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-3930), rpoD (protein.P00579), rpoS (protein.P13445), csgD (protein.P52106).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P52107|protein.P52107]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[complex.ecocyc.CPLX0-3930|complex.ecocyc.CPLX0-3930]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=csgC; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=csgC; function=+
- `activates` <-- [[protein.P52106|protein.P52106]] `RegulonDB` `S` - regulator=CsgD; target=csgC; function=+
- `represses` <-- [[protein.P0AFT5|protein.P0AFT5]] `RegulonDB` `S` - regulator=BtsR; target=csgC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003542,ECOCYC:G6548,GeneID:945623`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1104961-1105293:+; feature_type=gene
