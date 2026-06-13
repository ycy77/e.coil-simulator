---
entity_id: "gene.b4258"
entity_type: "gene"
name: "valS"
source_database: "NCBI RefSeq"
source_id: "gene-b4258"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4258"
  - "valS"
---

# valS

`gene.b4258`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4258`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

valS (gene.b4258) is a gene entity. It encodes valS (protein.P07118). Encoded protein function: FUNCTION: Catalyzes the attachment of valine to tRNA(Val). As ValRS can inadvertently accommodate and process structurally similar amino acids such as threonine, to avoid such errors, it has a 'posttransfer' editing activity that hydrolyzes mischarged Thr-tRNA(Val) in a tRNA-dependent manner. EcoCyc product frame: VALS-MONOMER. EcoCyc synonyms: val-act. Genomic coordinates: 4480982-4483837. EcoCyc protein note: Valine-tRNA ligase (ValRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. ValRS belongs to the Class I aminoacyl-tRNA synthetases . ValRS contains a conserved proline triplet that is critical for activity; it therefore requires EG12099-MONOMER EF-P for expression, which may explain evolution of the EF-P system . ValRS is a monomer in solution . A single binding site for tRNAVal was thought to exist , but evidence for a second binding site has been reported . The reaction mechanism of ValRS includes the formation of an aminoacyl adenylate intermediate, which then serves as the animo acid donor in the aminoacyl-tRNA synthetase reaction . The enzyme rapidly forms a valyl-adenylate and binds a second molecule of valine slowly...

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07118|protein.P07118]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=valS; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=valS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013946,ECOCYC:EG11067,GeneID:948785`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4480982-4483837:-; feature_type=gene
