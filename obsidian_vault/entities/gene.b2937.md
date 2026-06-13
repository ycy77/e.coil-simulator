---
entity_id: "gene.b2937"
entity_type: "gene"
name: "speB"
source_database: "NCBI RefSeq"
source_id: "gene-b2937"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2937"
  - "speB"
---

# speB

`gene.b2937`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2937`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

speB (gene.b2937) is a gene entity. It encodes speB (protein.P60651). Encoded protein function: FUNCTION: Catalyzes the formation of putrescine from agmatine. {ECO:0000269|PubMed:10527864}. EcoCyc product frame: AGMATIN-MONOMER. Genomic coordinates: 3082877-3083797. EcoCyc protein note: Agmatinase (SpeB) catalyzes the hydrolysis of agmatine to yield urea and putrescine, the product of the PWY-40 pathway . Crystal stuctures of SpeB have been solved . While the enzyme was initially thought to be homodimeric in solution , the crystal structures and gel filtration data agree on a homohexameric quarternary structure . One molecule of Mn2+ is present per SpeB monomer . The His163Phe , Asp153Asn , His126Asn, His151Asn and Glu174Ala mutations leads to loss of activity. Based on the structural and mutant data, a catalytic mechanism was proposed . Agmatinase activity is induced by the presence of its substrate, agmatine , as well as L-arginine . Experiments determining regulation of agmatinase activity by cAMP yielded contradictory results . later showed that the effect of cAMP on SpeB expression is indirect. Agmatinase synthesis is also controlled by nitrogen availability . The EG11291-MONOMER appears to enhance expression of agmatinase...

## Biological Role

Repressed by purR (protein.P0ACP7). Activated by rpoS (protein.P13445).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60651|protein.P60651]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=speB; function=+
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=speB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009632,ECOCYC:EG10960,GeneID:947715`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3082877-3083797:-; feature_type=gene
