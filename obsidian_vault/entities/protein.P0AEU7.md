---
entity_id: "protein.P0AEU7"
entity_type: "protein"
name: "skp"
source_database: "UniProt"
source_id: "P0AEU7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:1838129, ECO:0000269|PubMed:8730870}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "skp hlpA ompH b0178 JW0173"
---

# skp

`protein.P0AEU7`

## Static

- Type: `protein`
- Source: `UniProt:P0AEU7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:1838129, ECO:0000269|PubMed:8730870}.

## Enriched Summary

FUNCTION: Molecular chaperone that interacts specifically with outer membrane proteins, thus maintaining the solubility of early folding intermediates during passage through the periplasm. Required for the efficient release of OmpA from the inner membrane, the maintenance of its solubility in the periplasm, and, in association with lipopolysaccharide (LPS), for the efficient folding and insertion of OmpA into the outer membrane. {ECO:0000269|PubMed:10455120, ECO:0000269|PubMed:11278858, ECO:0000269|PubMed:12509434, ECO:0000269|PubMed:8730870, ECO:0000269|PubMed:9914480}. Skp is a periplasmic chaperone which functions during the biogenesis of outer membrane proteins (OMPs). Skp prevents folding of EG10669-MONOMER OmpA in solution; Skp and lipopolysaccharide (LPS) improve insertion of OmpA into phospholipid bilayers . Skp prevents EG12180-MONOMER PagP aggregation in vitro and accelerates PagP folding into negatively charged liposomes . Skp interacts with OmpA and PhoE in close proximity to the inner membrane; Skp interacts with early folding intermediates of outer membrane proteins . Purifed Skp prevents the aggregation of lysozyme in a nucleotide independent manner . skp::Tn10 mutation induces the RPOE-MONOMER sigma E regulon . Mutational inactivation of skp results in decreased abundance of outer membrane proteins, compared to wild type...

## Biological Role

Component of periplasmic chaperone Skp (complex.ecocyc.CPLX0-7711).

## Annotation

FUNCTION: Molecular chaperone that interacts specifically with outer membrane proteins, thus maintaining the solubility of early folding intermediates during passage through the periplasm. Required for the efficient release of OmpA from the inner membrane, the maintenance of its solubility in the periplasm, and, in association with lipopolysaccharide (LPS), for the efficient folding and insertion of OmpA into the outer membrane. {ECO:0000269|PubMed:10455120, ECO:0000269|PubMed:11278858, ECO:0000269|PubMed:12509434, ECO:0000269|PubMed:8730870, ECO:0000269|PubMed:9914480}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7711|complex.ecocyc.CPLX0-7711]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b0178|gene.b0178]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEU7`
- `KEGG:ecj:JW0173;eco:b0178;ecoc:C3026_00815;`
- `GeneID:86862688;93777247;944861;`
- `GO:GO:0001530; GO:0005829; GO:0006457; GO:0030288; GO:0042802; GO:0043165; GO:0050821; GO:0051082; GO:0051604`

## Notes

Chaperone protein Skp (DNA-binding 17 kDa protein) (Histone-like protein HLP-1) (Seventeen kilodalton protein)
