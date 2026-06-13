---
entity_id: "gene.b1656"
entity_type: "gene"
name: "sodB"
source_database: "NCBI RefSeq"
source_id: "gene-b1656"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1656"
  - "sodB"
---

# sodB

`gene.b1656`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1656`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sodB (gene.b1656) is a gene entity. It encodes sodB (protein.P0AGD3). Encoded protein function: FUNCTION: Destroys superoxide anion radicals which are normally produced within the cells and which are toxic to biological systems. EcoCyc product frame: SUPEROX-DISMUTFE-MONOMER. Genomic coordinates: 1735378-1735959. EcoCyc protein note: SodB, or FeSOD, is one of three superoxide dismutases in E. coli . The three enzymes differ in their metal cofactor requirement; FeSOD contains iron. Superoxide dismutase is implicated in the response to a large number of environmental changes that lead to the generation of superoxide radicals. FeSOD and the manganese-containing enzyme MnSOD (SodA) are not functionally equivalent; MnSOD is more effective than FeSOD in preventing damage to DNA, while FeSOD seems more effective in protecting a cytoplasmic superoxide-sensitive enzyme . However, both enzymes were shown to protect dihydroxy acid dehydratase from inactivation by oxidative stress . The reaction mechanism involves cycling of the metal ion between the +3 and +2 oxidation states; the midpoint potential of the metal ion determines what redox reactions are possible, and is thus precisely tuned . Crystal structures of FeSOD have been solved . Tyr34 is required for maximal activity ; its contribution to substrate binding has been evaluated...

## Biological Role

Repressed by ryhB (gene.b4451), fnrS (gene.b4699). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco04146` Peroxisome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGD3|protein.P0AGD3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=sodB; function=+
- `represses` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=sodB; function=-
- `represses` <-- [[gene.b4699|gene.b4699]] `RegulonDB` `S` - regulator=FnrS; target=sodB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005537,ECOCYC:EG10954,GeneID:944953`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1735378-1735959:+; feature_type=gene
