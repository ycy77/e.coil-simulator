---
entity_id: "gene.b1563"
entity_type: "gene"
name: "relE"
source_database: "NCBI RefSeq"
source_id: "gene-b1563"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1563"
  - "relE"
---

# relE

`gene.b1563`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1563`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

relE (gene.b1563) is a gene entity. It encodes relE (protein.P0C077). Encoded protein function: FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system (PubMed:9767574). A sequence-specific, ribosome-dependent mRNA endoribonuclease that inhibits translation during amino acid starvation (the stringent response). In vitro acts by cleaving mRNA with high codon specificity in the ribosomal A site between positions 2 and 3. The stop codon UAG is cleaved at a fast rate while UAA and UGA are cleaved with intermediate and slow rates. In vitro mRNA cleavage can also occur in the ribosomal E site after peptide release from peptidyl-tRNA in the P site as well as on free 30S subunits (PubMed:12526800). In vivo cuts frequently in the first 100 codons, most frequently after the second and third base and rarely near the stop codon (PubMed:21324908). Overexpression of RelE results in the inhibition of bacterial growth and a sharp decrease in colony-forming ability which is neutralized by the labile cognate antitoxin RelB. Overexpression also sharply increases persisters (cells that neither grow nor die in the presence of bactericidal agents and are largely responsible for high levels of biofilm tolerance to antimicrobials) (PubMed:15576765)...

## Biological Role

Repressed by relB (protein.P0C079). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C077|protein.P0C077]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=relE; function=+
- `represses` <-- [[protein.P0C079|protein.P0C079]] `RegulonDB` `S` - regulator=RelB; target=relE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005221,ECOCYC:EG11131,GeneID:947549`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1645346-1645633:-; feature_type=gene
