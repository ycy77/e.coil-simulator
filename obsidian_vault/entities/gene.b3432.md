---
entity_id: "gene.b3432"
entity_type: "gene"
name: "glgB"
source_database: "NCBI RefSeq"
source_id: "gene-b3432"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3432"
  - "glgB"
---

# glgB

`gene.b3432`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3432`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glgB (gene.b3432) is a gene entity. It encodes glgB (protein.P07762). Encoded protein function: FUNCTION: Catalyzes the formation of the alpha-1,6-glucosidic linkages in glycogen by scission of a 1,4-alpha-linked oligosaccharide from growing alpha-1,4-glucan chains and the subsequent attachment of the oligosaccharide to the alpha-1,6 position. {ECO:0000250}. EcoCyc product frame: GLYCOGEN-BRANCH-MONOMER. Genomic coordinates: 3571316-3573502. EcoCyc protein note: Gycogen branching enzyme (GlgB) belongs to the glycosyl hydrolase GH13 family of enzymes and catalyzes the formation of the branched α-1,6-glucosidic linkages from the growing α-1,4-glucan chain during glycogen biosynthesis. When cells are grown in Kornberg medium, a threshold level of around 4 nmoles (dry weight) of ppGpp is necessary to trigger net glycogen accumulation . Biochemical studies of the enzyme have been performed using E. coli B . Gycogen branching enzyme has a preference for transferring chains between 5 and 16 glucose units. The minimum chain length required for branching is 12 . The enzyme appears to prefer A chains as acceptors and to form branch linkages at the third glucose residue from the reducing end of the acceptor chain . The reaction products of N-terminally truncated enzymes show an altered branching pattern...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07762|protein.P07762]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=glgB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011209,ECOCYC:EG10378,GeneID:947940`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3571316-3573502:-; feature_type=gene
