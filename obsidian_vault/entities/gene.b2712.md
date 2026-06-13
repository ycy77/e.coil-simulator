---
entity_id: "gene.b2712"
entity_type: "gene"
name: "hypF"
source_database: "NCBI RefSeq"
source_id: "gene-b2712"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2712"
  - "hypF"
---

# hypF

`gene.b2712`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2712`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hypF (gene.b2712) is a gene entity. It encodes hypF (protein.P30131). Encoded protein function: FUNCTION: Involved in the maturation of [NiFe] hydrogenases (PubMed:12377778, PubMed:12586941, PubMed:8661925). Along with HypE, it catalyzes the synthesis of the CN ligands of the active site iron of [NiFe]-hydrogenases (PubMed:12586941). HypF functions as a carbamoyl transferase using carbamoylphosphate as a substrate and transferring the carboxamido moiety in an ATP-dependent reaction to the thiolate of the C-terminal cysteine of HypE yielding a protein-S-carboxamide (PubMed:12586941, PubMed:15291820). In the absence of any other substrate, displays carbamoyl-phosphate phosphatase activity (PubMed:12377778). {ECO:0000269|PubMed:12377778, ECO:0000269|PubMed:12586941, ECO:0000269|PubMed:15291820, ECO:0000269|PubMed:8661925}. EcoCyc product frame: EG11551-MONOMER. EcoCyc synonyms: hydA. Genomic coordinates: 2835173-2837425. EcoCyc protein note: HypF is one of a number of proteins required for maturation of FORMHYDROGI-CPLX, FORMHYDROG2-CPLX and HYDROG3-CPLX . In the absence of other substrates, HypF hydrolyzes carbamoyl phosphate . However, under physiological conditions in the presence of EG10487-MONOMER HypE, HypF functions as a carbamoyl transferase, generating MONOMER0-4166 at the C-terminal cysteine residue of HypE...

## Biological Role

Repressed by cra (protein.P0ACP1). Activated by fhlA (protein.P19323).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30131|protein.P30131]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P19323|protein.P19323]] `RegulonDB` `S` - regulator=FhlA; target=hypF; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=hypF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008915,ECOCYC:EG11551,GeneID:944963`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2835173-2837425:-; feature_type=gene
