---
entity_id: "protein.P64578"
entity_type: "protein"
name: "higB"
source_database: "UniProt"
source_id: "P64578"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "higB ygjN b3083 JW3054"
---

# higB

`protein.P64578`

## Static

- Type: `protein`
- Source: `UniProt:P64578`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. A probable translation-dependent mRNA interferase. Overexpression causes cessation of cell growth and inhibits cell proliferation via inhibition of translation; this blockage is overcome by subsequent expression of antitoxin HigA. Overexpression causes cleavage of a number of mRNAs in a translation-dependent fashion, suggesting this is an mRNA interferase. {ECO:0000269|PubMed:19943910}. HigB is the toxin of the HigB-HigA toxin-antitoxin system, acting as a translation-dependent mRNA interferase. HigB inhibits protein synthesis by cleaving translated mRNAs within the coding region . It also is a BECR-fold toxin in the RelE/ParE superfamily of type II toxin-antitoxin systems . An analysis of the targets and site specificity showed that HigB favors a G nucleotide downstream of the cleavage site and shows strong codon position preference. Like other E. coli endoribonuclease toxins, HigB activity does not affect mature ribosomes, but inhibits ribosome biogenesis, likely by affecting the translation of a specific set of ribosomal proteins . The crystal structure of the HigBA toxin-antitoxin complex suggests that the putative HigB active site is not occluded in the complex . Ectopic expression of HigB causes inhibition of cell growth...

## Biological Role

Catalyzes RXN0-5509 (reaction.ecocyc.RXN0-5509). Component of HigB-HigA toxin/antitoxin complex and DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-8230).

## Annotation

FUNCTION: Toxic component of a type II toxin-antitoxin (TA) system. A probable translation-dependent mRNA interferase. Overexpression causes cessation of cell growth and inhibits cell proliferation via inhibition of translation; this blockage is overcome by subsequent expression of antitoxin HigA. Overexpression causes cleavage of a number of mRNAs in a translation-dependent fashion, suggesting this is an mRNA interferase. {ECO:0000269|PubMed:19943910}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5509|reaction.ecocyc.RXN0-5509]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-8230|complex.ecocyc.CPLX0-8230]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3083|gene.b3083]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P64578`
- `KEGG:ecj:JW3054;eco:b3083;ecoc:C3026_16835;`
- `GeneID:89517935;93778904;947591;`
- `GO:GO:0003723; GO:0004521; GO:0006355; GO:0016787; GO:0017148; GO:0040008; GO:0043488; GO:0110001`
- `EC:3.1.-.-`

## Notes

mRNA interferase toxin HigB (EC 3.1.-.-) (Endoribonuclease HigB) (Toxin HigB)
