---
entity_id: "protein.P0C077"
entity_type: "protein"
name: "relE"
source_database: "UniProt"
source_id: "P0C077"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "relE b1563 JW1555"
---

# relE

`protein.P0C077`

## Static

- Type: `protein`
- Source: `UniProt:P0C077`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system (PubMed:9767574). A sequence-specific, ribosome-dependent mRNA endoribonuclease that inhibits translation during amino acid starvation (the stringent response). In vitro acts by cleaving mRNA with high codon specificity in the ribosomal A site between positions 2 and 3. The stop codon UAG is cleaved at a fast rate while UAA and UGA are cleaved with intermediate and slow rates. In vitro mRNA cleavage can also occur in the ribosomal E site after peptide release from peptidyl-tRNA in the P site as well as on free 30S subunits (PubMed:12526800). In vivo cuts frequently in the first 100 codons, most frequently after the second and third base and rarely near the stop codon (PubMed:21324908). Overexpression of RelE results in the inhibition of bacterial growth and a sharp decrease in colony-forming ability which is neutralized by the labile cognate antitoxin RelB. Overexpression also sharply increases persisters (cells that neither grow nor die in the presence of bactericidal agents and are largely responsible for high levels of biofilm tolerance to antimicrobials) (PubMed:15576765)...

## Biological Role

Catalyzes RXN0-5509 (reaction.ecocyc.RXN0-5509). Component of RelB-RelE antitoxin/toxin complex / DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-7791).

## Annotation

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system (PubMed:9767574). A sequence-specific, ribosome-dependent mRNA endoribonuclease that inhibits translation during amino acid starvation (the stringent response). In vitro acts by cleaving mRNA with high codon specificity in the ribosomal A site between positions 2 and 3. The stop codon UAG is cleaved at a fast rate while UAA and UGA are cleaved with intermediate and slow rates. In vitro mRNA cleavage can also occur in the ribosomal E site after peptide release from peptidyl-tRNA in the P site as well as on free 30S subunits (PubMed:12526800). In vivo cuts frequently in the first 100 codons, most frequently after the second and third base and rarely near the stop codon (PubMed:21324908). Overexpression of RelE results in the inhibition of bacterial growth and a sharp decrease in colony-forming ability which is neutralized by the labile cognate antitoxin RelB. Overexpression also sharply increases persisters (cells that neither grow nor die in the presence of bactericidal agents and are largely responsible for high levels of biofilm tolerance to antimicrobials) (PubMed:15576765). Plays a role in dormancy when expressed in high-density cells in the absence of antitoxin RelB; amino acid starvation and an unidentified extracellular factor promote dormancy, while expression of antitoxin RelB restores cell culturability (PubMed:22210768). Acts with RelB as a corepressor of relBE transcription, considerably increasing the repression of RelB alone. 2 RelB dimers bind to 2 operator sequences; DNA-binding and repression is stronger when complexed with toxin/corepressor RelE by conditional cooperativity (PubMed:18501926, PubMed:19747491, PubMed:22981948, PubMed:9767574). {ECO:0000269|PubMed:11274135, ECO:0000269|PubMed:11717402, ECO:0000269|PubMed:12123459, ECO:0000269|PubMed:12526800, ECO:0000269|PubMed:15576765, ECO:0000269|PubMed:18501926, ECO:0000269|PubMed:18532983, ECO:0000269|PubMed:19747491, ECO:0000269|PubMed:20005802, ECO:0000269|PubMed:21324908, ECO:0000269|PubMed:22210768, ECO:0000269|PubMed:22981948, ECO:0000269|PubMed:24251350, ECO:0000269|PubMed:9767574}.; FUNCTION: Seems to be a principal mediator of cell death in liquid media (PubMed:19707553). Implicated in hydroxy radical-mediated cell death induced by hydroxyurea treatment (PubMed:20005847). {ECO:0000269|PubMed:19707553, ECO:0000269|PubMed:20005847}.; FUNCTION: Cross-talk can occur between different TA systems. Ectopic expression of this toxin induces transcription of 7 tested TA systems (dinJ/yafQ, hicAB, mazEF, mqsRA, prlF(sohA)/yhaV, relBEF and yefM/yoeB) with specific cleavage of the relBEF mRNA produced immediately upstream and within the relB coding sequence. The cleaved mRNA can be translated into RelE, leading to a positive feedback cycle of RelE expression. The relBEF operon is required for transcription of the mazEF TA system operon during amino acid starvation. {ECO:0000269|PubMed:23432955}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5509|reaction.ecocyc.RXN0-5509]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-7791|complex.ecocyc.CPLX0-7791]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1563|gene.b1563]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C077`
- `KEGG:ecj:JW1555;eco:b1563;ecoc:C3026_09020;`
- `GeneID:947549;99778184;`
- `GO:GO:0000976; GO:0001217; GO:0004519; GO:0004521; GO:0006355; GO:0006402; GO:0016787; GO:0017148; GO:0019843; GO:0032993; GO:0034198; GO:0040008; GO:0043022; GO:0044010; GO:0046677; GO:0097351; GO:0110001`
- `EC:3.1.-.-`

## Notes

mRNA interferase toxin RelE (EC 3.1.-.-) (Endoribonuclease RelE) (Toxin RelE)
