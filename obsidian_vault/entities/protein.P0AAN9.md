---
entity_id: "protein.P0AAN9"
entity_type: "protein"
name: "iraP"
source_database: "UniProt"
source_id: "P0AAN9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "iraP yaiB b0382 JW0373"
---

# iraP

`protein.P0AAN9`

## Static

- Type: `protein`
- Source: `UniProt:P0AAN9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Inhibits RpoS proteolysis by regulating RssB activity, thereby increasing the stability of the sigma stress factor RpoS especially during phosphate starvation, but also in stationary phase and during nitrogen starvation. Its effect on RpoS stability is due to its interaction with RssB, which probably blocks the interaction of RssB with RpoS, and the consequent delivery of the RssB-RpoS complex to the ClpXP protein degradation pathway. {ECO:0000269|PubMed:16600914, ECO:0000269|PubMed:18383615}. IraP is one of several small anti-adaptor proteins; it is required for stabilization of the alternative sigma factor RPOS-MONOMER σS during phosphate starvation and plays a role in stationary phase and nitrogen starvation. The EG12121-MONOMER RssB adaptor protein binds to σS and targets it to the ClpXP protease for degradation. IraP does not affect the level or stability of RssB, but interferes directly with RssB-mediated degradation of σS by interacting with RssB . Each anti-adaptor protein interacts with RssB in a unique way . IraP does not inactivate ClpXP . Expression of iraP is induced by phosphate starvation; the effect is mediated by ppGpp and requires SpoT, but not RelA . CsgD was also shown to induce iraP expression . IraP is one of a number of proteins with high UUX Leucine codon usage (HULC proteins)...

## Annotation

FUNCTION: Inhibits RpoS proteolysis by regulating RssB activity, thereby increasing the stability of the sigma stress factor RpoS especially during phosphate starvation, but also in stationary phase and during nitrogen starvation. Its effect on RpoS stability is due to its interaction with RssB, which probably blocks the interaction of RssB with RpoS, and the consequent delivery of the RssB-RpoS complex to the ClpXP protein degradation pathway. {ECO:0000269|PubMed:16600914, ECO:0000269|PubMed:18383615}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0382|gene.b0382]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAN9`
- `KEGG:ecj:JW0373;eco:b0382;ecoc:C3026_01850;`
- `GeneID:93777080;947709;`
- `GO:GO:0005737; GO:0016036; GO:0042177; GO:0043856`

## Notes

Anti-adapter protein IraP
