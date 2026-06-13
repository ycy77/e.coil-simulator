---
entity_id: "gene.b1092"
entity_type: "gene"
name: "fabD"
source_database: "NCBI RefSeq"
source_id: "gene-b1092"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1092"
  - "fabD"
---

# fabD

`gene.b1092`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1092`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fabD (gene.b1092) is a gene entity. It encodes fabD (protein.P0AAI9). Encoded protein function: Malonyl CoA-acyl carrier protein transacylase (MCT) (EC 2.3.1.39) EcoCyc product frame: MALONYL-COA-ACP-TRANSACYL-MONOMER. EcoCyc synonyms: tfpA. Genomic coordinates: 1149728-1150657. EcoCyc protein note: Malonyl-CoA-acyl carrier protein transacylase (FabD) catalyzes the first committed step in the initiation of fatty acid biosynthesis, the transfer of the malonyl group from malonyl-CoA to acyl carrier protein (ACP) to form malonyl-ACP. Initial biochemical studies were performed on the enzyme purified from E. coli B . These studies showed that a malonyl-enzyme intermediate is formed during the reaction . The reaction utilizes a ping-pong bi bi mechanism . Crystal structures of FabD alone and in various binary complexes have been solved . In a crystal structure obtained after soaking in the substrate malonyl-CoA, its thioester bond has been cleaved, and the malonyl moiety is covalently bound to the active-site Ser92 residue via an oxo-ester bond. A detailed reaction mechanism has been described . Arg117 is an active site residue that interacts with the carboxylate of the malonyl-FabD reaction intermediate...

## Biological Role

Activated by rpoD (protein.P00579), fadR (protein.P0A8V6).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco00074` Mycolic acid biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAI9|protein.P0AAI9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fabD; function=+
- `activates` <-- [[protein.P0A8V6|protein.P0A8V6]] `RegulonDB` `C` - regulator=FadR; target=fabD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003698,ECOCYC:EG11317,GeneID:945766`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1149728-1150657:+; feature_type=gene
