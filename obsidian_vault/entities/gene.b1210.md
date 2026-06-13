---
entity_id: "gene.b1210"
entity_type: "gene"
name: "hemA"
source_database: "NCBI RefSeq"
source_id: "gene-b1210"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1210"
  - "hemA"
---

# hemA

`gene.b1210`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1210`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hemA (gene.b1210) is a gene entity. It encodes hemA (protein.P0A6X1). Encoded protein function: FUNCTION: Catalyzes the NADPH-dependent reduction of glutamyl-tRNA(Glu) to glutamate 1-semialdehyde (GSA). In the absence of NADPH, exhibits substrate esterase activity, leading to the release of glutamate from tRNA. {ECO:0000269|PubMed:12370189, ECO:0000269|PubMed:1569081}. EcoCyc product frame: GLUTRNAREDUCT-MONOMER. EcoCyc synonyms: gtrA. Genomic coordinates: 1263714-1264970. EcoCyc protein note: Glutamyl-tRNA reductase catalyzes the first step of porphyrin biosynthesis. The reaction appears to proceed via a thioester intermediate . Determinants for recognition of Glu-tRNA(Glu) by the enzyme have been studied . HemA can be isolated in multiple multimeric forms, but the dimer may represent the functional form of the enzyme . The HemA dimer forms a tight complex with glutamate-1-semialdehyde 2,1-aminomutase, the second enzyme in the pathway, suggesting metabolic channeling of the highly reactive intermediate glutamate-1-semialdehyde . Heme limitation leads to an increase in abundance of HemA protein , although only a 3-fold increase in hemA expression can be detected . In Salmonella typhimurium, HemA abundance appears to be increased by stabilization of the protein...

## Biological Role

Repressed by fnr (protein.P0A9E5). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6X1|protein.P0A6X1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hemA; function=+
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=hemA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004064,ECOCYC:EG10427,GeneID:945777`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1263714-1264970:+; feature_type=gene
