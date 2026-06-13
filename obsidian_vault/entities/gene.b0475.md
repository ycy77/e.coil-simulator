---
entity_id: "gene.b0475"
entity_type: "gene"
name: "hemH"
source_database: "NCBI RefSeq"
source_id: "gene-b0475"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0475"
  - "hemH"
---

# hemH

`gene.b0475`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0475`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hemH (gene.b0475) is a gene entity. It encodes hemH (protein.P23871). Encoded protein function: FUNCTION: Catalyzes the ferrous insertion into protoporphyrin IX. {ECO:0000255|HAMAP-Rule:MF_00323}. EcoCyc product frame: PROTOHEME-FERROCHELAT-MONOMER. EcoCyc synonyms: popA, visA. Genomic coordinates: 498055-499017. EcoCyc protein note: Ferrochelatase is the terminal enzyme in the heme biosynthesis pathway and catalyzes the insertion of Fe2+ into protoporphyrin IX. Both eukaryotic and some microbial ferrochelatases have been shown to contain a [2Fe-2S] cluster ; however, no studies have been performed with the E. coli enzyme. A hemH mutant is sensitive to visible light due to the accumulation of protoporphyrin IX. This is similar to the defect observed in human protoporphyria . The defect in iron incorporation into protoporphyrin IX in a hemH mutant results in a defect in assembly of membrane-associated succinate-ubiquinone reductase . Expression of hemH is mildly regulated in response to heme availability and is activated by OxyR . VisA: "visible light-sensitive" HemH: "heme biosynthesis" Reviews:

## Biological Role

Repressed by nac (protein.Q47005). Activated by oxyR (protein.P0ACQ4).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23871|protein.P23871]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `S` - regulator=OxyR; target=hemH; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=hemH; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001649,ECOCYC:EG10431,GeneID:947532`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:498055-499017:+; feature_type=gene
