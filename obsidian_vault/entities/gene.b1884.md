---
entity_id: "gene.b1884"
entity_type: "gene"
name: "cheR"
source_database: "NCBI RefSeq"
source_id: "gene-b1884"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1884"
  - "cheR"
---

# cheR

`gene.b1884`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1884`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cheR (gene.b1884) is a gene entity. It encodes cheR (protein.P07364). Encoded protein function: FUNCTION: Methylation of the membrane-bound methyl-accepting chemotaxis proteins (MCP) to form gamma-glutamyl methyl ester residues in MCP. EcoCyc product frame: CHER-MONOMER. EcoCyc synonyms: cheX. Genomic coordinates: 1968504-1969364. EcoCyc protein note: cheR encodes an S-adenosylmethionine-dependent methyltransferase; CheR methylates specific glutamate residues in the cytoplasmic domains of the methyl-accepting chemotaxis proteins (MCPs) CPLX0-8103 "Tsr", CPLX0-8102 "Tar", CPLX0-8105 "Trg" and CPLX0-8104 "Tap". Together, the CheR methyltransferase and the CHEB-MONOMER "CheB" deamidase/methylesterase modulate the level of chemoreceptor methylation in a feedback loop that enables the cell to adapt to chemotactic stimuli (see reviews ). In the absence of chemoeffector gradients the adaption enzymes CheR and CheB promote synchronous rotational switching of flagellar motors which supports the characteristic run-and-tumble swimming behaviour . CheR, from Salmonella typhimurium has been well characterized and used in experiments examining methylation of E. coli chemoreceptors (see for example ); the S. typhimurium CheR methyltransferase is expected to be functionally identical to the E. coli homolog...

## Biological Role

Activated by fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P07364|protein.P07364]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=cheR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006286,ECOCYC:EG10148,GeneID:946396`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1968504-1969364:-; feature_type=gene
