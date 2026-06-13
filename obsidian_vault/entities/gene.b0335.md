---
entity_id: "gene.b0335"
entity_type: "gene"
name: "prpE"
source_database: "NCBI RefSeq"
source_id: "gene-b0335"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0335"
  - "prpE"
---

# prpE

`gene.b0335`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0335`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

prpE (gene.b0335) is a gene entity. It encodes prpE (protein.P77495). Encoded protein function: FUNCTION: Catalyzes the synthesis of propionyl-CoA from propionate and CoA. Also converts acetate to acetyl-CoA but with a lower specific activity (By similarity). {ECO:0000250}. EcoCyc product frame: G6200-MONOMER. EcoCyc synonyms: yahU. Genomic coordinates: 352706-354592. EcoCyc protein note: Propionyl-CoA synthetase catalyzes formation of propinoyl-CoA, the first reaction in propionate catabolism via the methylcitrate cycle. The prpE-encoded propionyl-CoA synthetase contains redox-active thiols that influence enzyme activity. PrpE is activated by DTT, which may reduce an intramolecular disulfide bond between C128 and C315. Like the orthologous enzyme from Salmonella enterica, it may also be activated by removal of a propionyl modification from an active site lysine residue . Overexpression of PrpE has been used as a tool in metabolic engineering of E. coli for heterologous polyketide production . did not detect the PrpE protein in a 2-D gel even during growth on propionate as the sole carbon source; thus, Acs appeared to be more likely than PrpE to catalyze the first step in the propionate metabolism pathway. In addition, showed that a Δacs mutant is unable to grow on propionate as the sole carbon and energy source. Expression of prpE is induced by propionate...

## Biological Role

Repressed by cra (protein.P0ACP1). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77495|protein.P77495]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=prpE; function=+
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=prpE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001154,ECOCYC:G6200,GeneID:946891`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:352706-354592:+; feature_type=gene
