---
entity_id: "gene.b0722"
entity_type: "gene"
name: "sdhD"
source_database: "NCBI RefSeq"
source_id: "gene-b0722"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0722"
  - "sdhD"
---

# sdhD

`gene.b0722`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0722`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sdhD (gene.b0722) is a gene entity. It encodes sdhD (protein.P0AC44). Encoded protein function: FUNCTION: Membrane-anchoring subunit of succinate dehydrogenase (SDH). EcoCyc product frame: SDH-MEMB2. EcoCyc synonyms: cybS, dhsD. Genomic coordinates: 755560-755907. EcoCyc protein note: One of two membrane proteins in the four subunit enzyme. SdhC and SdhD are the large and small subunits of cytochrome b556, respectively . The b556 type heme bridges both membrane subunits . Published reports disagree about whether mutation of SdhC-[His84] or SdhD-[His71] residues eliminate coordination of the heme b . Mutation of the residues coordinating the heme indicate that the heme helps stabilize the enzyme . SdhC-[His84] is involved in interaction with the quinone electron acceptor . SdhC-[His84] and SdhD-[His71] (with the associated heme b) are reported to be dispensable for assembly, while SdhC-[His30] is required for proper assembly of the membrane-bound enzyme . Mutants lacking SdhC and SdhD show cytoplasmic succinate dehydrogenase activity using artificial electron acceptors, in contrast to wild-type membrane-associated succinate-ubiquinone oxidoreductase activity...

## Biological Role

Repressed by fur (protein.P0A9A9), arcA (protein.P0A9Q1). Activated by fur (protein.P0A9A9), arcA (protein.P0A9Q1), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC44|protein.P0AC44]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=sdhD; function=-+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=sdhD; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=sdhD; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=sdhD; function=-+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=sdhD; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0002464,ECOCYC:EG10934,GeneID:945322`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:755560-755907:+; feature_type=gene
