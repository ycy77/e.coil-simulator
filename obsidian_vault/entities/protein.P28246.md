---
entity_id: "protein.P28246"
entity_type: "protein"
name: "bcr"
source_database: "UniProt"
source_id: "P28246"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000305|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bcr bicA bicR sur suxA b2182 JW5363"
---

# bcr

`protein.P28246`

## Static

- Type: `protein`
- Source: `UniProt:P28246`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000305|PubMed:15919996}.

## Enriched Summary

FUNCTION: Involved in sulfonamide (sulfathiazole) and bicyclomycin resistance (PubMed:2694948). Probable membrane translocase. A transporter able to export peptides. When overexpressed, allows cells deleted for multiple peptidases (pepA, pepB, pepD and pepN) to grow in the presence of dipeptides Ala-Gln or Gly-Tyr which otherwise inhibit growth (PubMed:20067529). Cells overexpressing this protein have decreased intracellular levels of Ala-Gln dipeptide, and in a system that produces the Ala-Gln dipeptide overproduction of this protein increases export of the dipeptide (PubMed:20067529). {ECO:0000269|PubMed:2694948}. Expression of bcr from a high-copy number plasmid confers resistance to the antibiotic bicyclomycin ; increased expression of bcr contributes to sulfathiazole resistance in an E. coli strain that also contains a sulfathiazole-resistant H2PTEROATESYNTH-MONOMER . Multicopy expression of bcr in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ), confers moderate resistance to tetracycline, fosfomycin, kanamycin and acriflavine but does not impact the resistance to a range of other antibiotics and toxic compounds . Bcr is able to transport dipeptides (Ala-Gln and L-alanyl-L-branched chain amino acids) in a dipeptide overproducing strain and promotes L-cysteine export in cells engineered for L-cysteine overproduction...

## Biological Role

Catalyzes bicozamycin:H+ antiport (reaction.ecocyc.TRANS-RXN-340), xenobiotic:proton antiport (reaction.ecocyc.TRANS-RXN-44). Transports bicozamycin (molecule.ecocyc.CPD-20921), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Involved in sulfonamide (sulfathiazole) and bicyclomycin resistance (PubMed:2694948). Probable membrane translocase. A transporter able to export peptides. When overexpressed, allows cells deleted for multiple peptidases (pepA, pepB, pepD and pepN) to grow in the presence of dipeptides Ala-Gln or Gly-Tyr which otherwise inhibit growth (PubMed:20067529). Cells overexpressing this protein have decreased intracellular levels of Ala-Gln dipeptide, and in a system that produces the Ala-Gln dipeptide overproduction of this protein increases export of the dipeptide (PubMed:20067529). {ECO:0000269|PubMed:2694948}.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-340|reaction.ecocyc.TRANS-RXN-340]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-44|reaction.ecocyc.TRANS-RXN-44]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CPD-20921|molecule.ecocyc.CPD-20921]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2182|gene.b2182]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P28246`
- `KEGG:ecj:JW5363;eco:b2182;ecoc:C3026_12205;`
- `GeneID:944808;`
- `GO:GO:0005886; GO:0015031; GO:0015385; GO:0033228; GO:0033229; GO:0035442; GO:0042910; GO:0046677; GO:0071916; GO:1990961`

## Notes

Bicyclomycin resistance protein (Sulfonamide resistance protein)
