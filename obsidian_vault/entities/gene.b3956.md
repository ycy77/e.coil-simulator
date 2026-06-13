---
entity_id: "gene.b3956"
entity_type: "gene"
name: "ppc"
source_database: "NCBI RefSeq"
source_id: "gene-b3956"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3956"
  - "ppc"
---

# ppc

`gene.b3956`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3956`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ppc (gene.b3956) is a gene entity. It encodes ppc (protein.P00864). Encoded protein function: FUNCTION: Forms oxaloacetate, a four-carbon dicarboxylic acid source for the tricarboxylic acid cycle. EcoCyc product frame: PEPCARBOX-MONOMER. EcoCyc synonyms: asp, glu. Genomic coordinates: 4150447-4153098. EcoCyc protein note: Phosphoenolpyruvate carboxylase (Ppc) is an anaplerotic enzyme that replenishes oxaloacetate in the tricarboxylic acid cycle. The carboxylation of phosphoenolpyruvate (PEP) to form oxaloacetate and Pi proceeds in two steps: formation of carboxyphosphate and the enolate form of pyruvate, followed by carboxylation of the enolate and release of phosphate and oxaloacetate. Ppc activity is allosterically regulated by many kinds of effectors that interact with several distinct binding sites. The in vivo concentrations of the various regulators differ depending on the growth conditions, resulting in different levels of enzyme activity . The primary activator was thought to be acetyl-CoA; fructose-1,6-bisphosphate (FBP) and GTP can act synergistically with acetyl-CoA . A mechanism for synergistic activaton of the enzyme by different effectors was proposed . In a proteome-wide screen, Ppc was found to bind citrate, ATP, and FBP. Citrate inhibits Ppc activity in vitro; the presence of FBP or acetyl-CoA had no effect on the inhibition...

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco00710` Carbon fixation by Calvin cycle (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00864|protein.P00864]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ppc; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ECOCYC:EG10756,GeneID:948457`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4150447-4153098:-; feature_type=gene
