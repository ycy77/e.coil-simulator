---
entity_id: "gene.b0507"
entity_type: "gene"
name: "gcl"
source_database: "NCBI RefSeq"
source_id: "gene-b0507"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0507"
  - "gcl"
---

# gcl

`gene.b0507`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0507`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gcl (gene.b0507) is a gene entity. It encodes gcl (protein.P0AEP7). Encoded protein function: FUNCTION: Catalyzes the condensation of two molecules of glyoxylate to give 2-hydroxy-3-oxopropanoate (also termed tartronate semialdehyde). EcoCyc product frame: GLYOCARBOLIG-MONOMER. Genomic coordinates: 533916-535697. EcoCyc protein note: Glyoxylate carboligase condenses two molecules of glyoxylate to form tartronate semialdehyde. The reaction takes place under completely anaerobic conditions . The enzyme requires FAD for activity, although the reaction catalyzed by glyoxylate carboligase has no oxidation or reduction step . It appears to be a dimer in solution . The protein sequence contains conserved quinone, thiamine diphosphate (ThDP) and FAD binding sites . A crystal structure of the enzyme has been solved at 2.7 Å resolution . Unlike other ThDP-dependent enzymes, glyoxylate carboligase does not contain the usually strictly conserved carboxylate group of glutamate within hydrogen bond distance of ThDP. Kinetic studies of the wild type and various mutant enzymes suggested an unusual activation mechanism for the thiazol cofactor . Glyoxylate carboligase activity is increased by growth on glycolate or glyoxylate as the sole source of carbon . gcl promoter activity and the kinetics of inductionby glyoxylate have been observed in single cells in real time...

## Biological Role

Repressed by allR (protein.P0ACN4).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEP7|protein.P0AEP7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACN4|protein.P0ACN4]] `RegulonDB` `C` - regulator=AllR; target=gcl; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001754,ECOCYC:EG11583,GeneID:945394`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:533916-535697:+; feature_type=gene
