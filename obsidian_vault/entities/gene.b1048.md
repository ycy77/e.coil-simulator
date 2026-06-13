---
entity_id: "gene.b1048"
entity_type: "gene"
name: "opgG"
source_database: "NCBI RefSeq"
source_id: "gene-b1048"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1048"
  - "opgG"
---

# opgG

`gene.b1048`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1048`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

opgG (gene.b1048) is a gene entity. It encodes mdoG (protein.P33136). Encoded protein function: FUNCTION: Involved in the biosynthesis of osmoregulated periplasmic glucans (OPGs). EcoCyc product frame: EG11885-MONOMER. EcoCyc synonyms: mdoA, mdoG. Genomic coordinates: 1109335-1110870. EcoCyc protein note: OpgG is a periplasmic protein that, along with the inner membrane glycosyltransferase EG11886-MONOMER OpgH, is required for synthesis of the branched periplasmic oligosaccharides known as CPD-16398 osmoregulated periplasmic glucans (OPGs), formerly called membrane-derived oligosaccharides (MDOs); although exact details remain unclear, an OpgGH complex is suggested to function for synthesis and translocation of the polyglucose backbone structure of OPG in a process requiring CPD-12575 UDP-glucose and EG50003-MONOMER acyl carrier protein (and see ). In the crystal structure reported by , OpgG contains a large N-terminal domain containing a potential active site and a smaller C-terminal domain. The precise function of OpgG is not known - it may interact with OpgH in the membrane and and it may play a role in forming the branch points of OPG. Early studies characterized mdoA mutants which were defective in OPG synthesis and exhibited pleiotropic phenotypes (also )...

## Biological Role

Activated by rpoD (protein.P00579), rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33136|protein.P33136]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=opgG; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=opgG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003558,ECOCYC:EG11885,GeneID:945005`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1109335-1110870:+; feature_type=gene
